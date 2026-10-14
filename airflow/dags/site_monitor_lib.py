"""Read-only Salar Cafe website monitoring, usable by Airflow or GitHub Actions.

No user-submitted statistical datasets or credentials are collected.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import time
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "data" / "all-public-urls.json"
REPORT_DIR = ROOT / "reports" / "airflow"
SITE = "https://onlineinternetcafe.com"
HOST = "onlineinternetcafe.com"
USER_AGENT = "SalarCafeHealthMonitor/1.0 (+https://onlineinternetcafe.com/)"
PINNED = (
    f"{SITE}/",
    f"{SITE}/statistical-calculators/",
    f"{SITE}/web-calculators/",
    f"{SITE}/ap-score-calculator/",
    f"{SITE}/differential-equation-solver/",
)
MAX_BYTES = 2_700_000


class PageMetadata(HTMLParser):
    """Extract only SEO tags without running scripts."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.h1_count = 0
        self.description = ""
        self.canonical = ""
        self.robots = ""

    def handle_starttag(self, tag, attrs):
        props = {k.lower(): (v or "") for k, v in attrs if k}
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta":
            name = props.get("name", "").lower()
            if name == "description":
                self.description = props.get("content", "").strip()
            elif name == "robots":
                self.robots = props.get("content", "").strip()
        elif tag == "link" and "canonical" in props.get("rel", "").lower().split():
            self.canonical = props.get("href", "").strip()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def valid_site_url(url):
    try:
        p = urlsplit(url)
        return (p.scheme == "https" and p.hostname == HOST
                and not p.username and not p.password
                and not p.query and not p.fragment
                and not p.path.lower().endswith((".xml", ".gz", ".pdf", ".csv", ".json")))
    except ValueError:
        return False


def load_catalog(path=None):
    path = path if path is not None else CATALOG_PATH
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("website") != SITE or not isinstance(payload.get("urls"), list):
        raise ValueError("Invalid Salar Cafe catalog format")
    urls = sorted({
        row["url"] for row in payload["urls"]
        if isinstance(row, dict) and isinstance(row.get("url"), str)
        and valid_site_url(row["url"])
    })
    if not urls:
        raise ValueError("Catalog contained no valid site URLs")
    return urls, payload.get("generated_utc", ""), payload.get("warnings", [])


def select_pages(urls, run_date, batch_size=120):
    """Fixed, non-overlapping daily batches until all catalog URLs have been covered."""
    batch_size = max(1, min(300, int(batch_size)))
    priority = [url for url in PINNED if url in urls]
    remaining = sorted(set(urls) - set(priority))
    batch_count = max(1, math.ceil(len(remaining) / batch_size))
    slot = (run_date.toordinal() - date(2026, 10, 15).toordinal()) % batch_count
    return priority + remaining[slot * batch_size:(slot + 1) * batch_size], slot, batch_count


def check_page(url, timeout=18):
    result = {"url": url, "status": None, "elapsed_ms": None, "bytes_read": 0, "issues": []}
    if not valid_site_url(url):
        result["issues"].append("unsafe_url")
        return result
    started = time.monotonic()
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
        with urlopen(req, timeout=timeout) as response:
            result["status"] = response.status
            result["elapsed_ms"] = round((time.monotonic() - started) * 1000)
            final_url = response.geturl()
            mime = response.headers.get("Content-Type", "")
            body = response.read(MAX_BYTES + 1)
            result["bytes_read"] = len(body)
            if not valid_site_url(final_url):
                result["issues"].append("unexpected_redirect")
            if response.status != 200:
                result["issues"].append(f"http_{response.status}")
            if "text/html" not in mime.lower():
                result["issues"].append("not_html")
                return result
            if len(body) > MAX_BYTES:
                result["issues"].append("large_html")
                body = body[:MAX_BYTES]
            parser = PageMetadata()
            parser.feed(body.decode("utf-8", errors="replace"))
            result.update({
                "title": parser.title.strip(),
                "h1_count": parser.h1_count,
                "canonical": parser.canonical,
                "description_present": bool(parser.description),
                "robots": parser.robots,
            })
            if not parser.title.strip():
                result["issues"].append("missing_title")
            if parser.h1_count == 0:
                result["issues"].append("missing_h1")
            elif parser.h1_count > 1:
                result["issues"].append("multiple_h1")
            if not parser.description:
                result["issues"].append("missing_meta_description")
            if not parser.canonical:
                result["issues"].append("missing_canonical")
            elif parser.canonical.rstrip("/") != url.rstrip("/"):
                result["issues"].append("canonical_mismatch")
            if "noindex" in parser.robots.lower().replace(" ", ""):
                result["issues"].append("noindex")
    except HTTPError as exc:
        result["status"] = exc.code
        result["issues"].append(f"http_{exc.code}")
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        result["issues"].append("request_failure")
        result["error_type"] = type(exc).__name__
    finally:
        if result["elapsed_ms"] is None:
            result["elapsed_ms"] = round((time.monotonic() - started) * 1000)
    return result


def get_wordpress_counts():
    """Only public aggregate counts, not private/admin endpoints."""
    out = {}
    for kind in ("pages", "posts"):
        url = f"{SITE}/wp-json/wp/v2/{kind}?per_page=1&_fields=id"
        try:
            with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=15) as resp:
                resp.read(2048)
                total = resp.headers.get("X-WP-Total")
                out[kind] = int(total) if total is not None else None
        except (HTTPError, URLError, TimeoutError, OSError, ValueError):
            out[kind] = None
    return out


def get_ga4_metrics(day):
    """Optional GA4 aggregate metrics; not enabled without private credentials."""
    property_id = os.getenv("GA4_PROPERTY_ID", "").strip()
    if not property_id or not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return {"status": "not_configured"}
    try:
        from google.analytics.data_v1beta import (
            BetaAnalyticsDataClient, DateRange, Metric, RunReportRequest
        )
        client = BetaAnalyticsDataClient()
        response = client.run_report(RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[DateRange(start_date=day.isoformat(), end_date=day.isoformat())],
            metrics=[Metric(name=name) for name in
                     ("sessions", "activeUsers", "screenPageViews")],
        ))
        values = [int(float(item.value)) for item in response.rows[0].metric_values] if response.rows else [0, 0, 0]
        return {"status": "ok", "date": day.isoformat(),
                "sessions": values[0], "active_users": values[1],
                "page_views": values[2]}
    except Exception as exc:
        return {"status": "error", "error_type": type(exc).__name__}


def load_previous(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def markdown_report(report):
    counts = report["issue_counts"]
    issues = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    ga = report["ga4"]
    lines = [
        f"# Salar Cafe daily health report — {report['date']}",
        "",
        f"- Catalog URLs: **{report['catalog_url_count']}** (snapshot {report['catalog_generated_utc'] or 'unknown'})",
        f"- Checked today: **{report['checked']}** (rotating batch {report['batch_slot']+1}/{report['batch_count']})",
        f"- HTTP 200: **{report['http_200']}**; other/no response: **{report['checked']-report['http_200']}**",
        f"- Pages with one or more flags: **{report['flagged']}**",
        f"- WordPress public pages/posts: **{report['wordpress'].get('pages')} / {report['wordpress'].get('posts')}**",
        f"- GA4: **{ga['status']}**" + (
            f" — sessions {ga['sessions']}, active users {ga['active_users']}, views {ga['page_views']} ({ga['date']})"
            if ga["status"] == "ok" else ""),
        "",
        "## Issue counts",
        "",
    ]
    lines.extend([f"- {name}: {number}" for name, number in issues] or ["No issues detected in sampled pages."])
    lines.extend(["", "## Flagged pages (first 40)", ""])
    flagged = [p for p in report["pages"] if p["issues"]]
    lines.extend([
        f"- HTTP {p['status'] or 'unknown'} | {p['url']} | {', '.join(p['issues'])}"
        for p in flagged[:40]
    ] or ["No flagged pages in this batch."])
    lines.extend(["", "## Coverage and interpretation", "",
        "Rotating URL audits cover the full catalog over multiple days; these numbers are not full-site defect totals.",
        "Checks are HTML/static-response checks, not browser-interaction or calculator-math correctness tests.",
        "GA4 visitor metrics require separately configured credentials and are never estimated from crawler counts.",
        "Reports contain only aggregate analytics and publicly available page metadata.",
        ""])
    return "\n".join(lines)


def run(run_date=None, batch_size=120, delay=0.15, output_dir=REPORT_DIR):
    run_date = run_date or datetime.now(timezone.utc).date()
    urls, catalog_created, warnings = load_catalog()
    selected, slot, batches = select_pages(urls, run_date, batch_size)
    pages = []
    for url in selected:
        pages.append(check_page(url))
        if delay:
            time.sleep(max(0.0, delay))
    counts = Counter(issue for page in pages for issue in page["issues"])
    previous = load_previous(Path(output_dir) / "latest.json")
    report = {
        "date": run_date.isoformat(),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "website": SITE,
        "catalog_url_count": len(urls),
        "catalog_generated_utc": catalog_created,
        "catalog_warnings": warnings[:20],
        "batch_slot": slot,
        "batch_count": batches,
        "checked": len(pages),
        "http_200": sum(p["status"] == 200 for p in pages),
        "flagged": sum(bool(p["issues"]) for p in pages),
        "issue_counts": dict(sorted(counts.items())),
        "wordpress": get_wordpress_counts(),
        "ga4": get_ga4_metrics(run_date - timedelta(days=1)),
        "previous_report_date": previous.get("date"),
        "pages": pages,
    }
    dest = Path(output_dir)
    dest.mkdir(parents=True, exist_ok=True)
    json_text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    md_text = markdown_report(report)
    for name, content in (
        (f"{run_date}.json", json_text),
        (f"{run_date}.md", md_text),
        ("latest.json", json_text),
        ("latest.md", md_text),
    ):
        (dest / name).write_text(content, encoding="utf-8")
    return {"date": report["date"], "checked": report["checked"],
            "http_200": report["http_200"], "flagged": report["flagged"],
            "report_path": str(dest / "latest.md")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", type=date.fromisoformat,
                        default=datetime.now(timezone.utc).date())
    parser.add_argument("--batch-size", type=int,
                        default=int(os.getenv("SALAR_BATCH_SIZE", "120")))
    parser.add_argument("--delay", type=float, default=0.15)
    args = parser.parse_args()
    print(json.dumps(run(run_date=args.date, batch_size=args.batch_size,
                         delay=args.delay), sort_keys=True))


if __name__ == "__main__":
    main()
