#!/usr/bin/env python3
"""Build a complete, refreshable directory of public onlineinternetcafe.com URLs.

The script reads the website's declared sitemap families, recursively expands sitemap
indexes, removes media/admin/non-page URLs, deduplicates canonical HTTPS URLs, and
writes Markdown, CSV, and JSON catalogs. It uses only Python's standard library so
it can run in GitHub Actions without installing packages.
"""

from __future__ import annotations

import csv
import gzip
import json
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlunparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

DOMAIN = "onlineinternetcafe.com"
BASE = f"https://{DOMAIN}"
SITEMAP_CANDIDATES = [
    f"{BASE}/sitemap_index.xml",
    f"{BASE}/sitemap.xml",
    f"{BASE}/wp-sitemap.xml",
    f"{BASE}/calculator-sitemap.xml",
]
USER_AGENT = (
    "Mozilla/5.0 (compatible; SalarCafeDirectoryBot/1.0; "
    "+https://github.com/yaarsaqib/salar-cafe-statistical-resources)"
)
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MARKDOWN_PATH = ROOT / "FULL-WEBSITE-DIRECTORY.md"
CSV_PATH = DATA_DIR / "all-public-urls.csv"
JSON_PATH = DATA_DIR / "all-public-urls.json"

# These are confirmed public hubs and high-value pages. They also act as a fallback
# if a temporary firewall or DNS problem prevents one sitemap from being read.
CONFIRMED_SEEDS = {
    f"{BASE}/",
    f"{BASE}/statistical-calculators/",
    f"{BASE}/ap-score-calculator/",
    f"{BASE}/calculator-sitemap.xml",
    f"{BASE}/sitemap_index.xml",
    f"{BASE}/differential-equation-solver/",
    f"{BASE}/physics-formula-solver/",
    f"{BASE}/equation-plotter-calculator/",
    f"{BASE}/chemical-reaction-calculator/",
}

EXCLUDED_PATH_PARTS = (
    "/wp-admin/",
    "/wp-json/",
    "/wp-content/uploads/",
    "/feed/",
    "/comments/",
    "/trackback/",
)


def fetch_bytes(url: str, attempts: int = 3) -> tuple[bytes, str]:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            request = Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "application/xml,text/xml,text/plain,*/*;q=0.8",
                },
            )
            with urlopen(request, timeout=35) as response:
                payload = response.read()
                final_url = response.geturl()
                encoding = (response.headers.get("Content-Encoding") or "").lower()
                if final_url.endswith(".gz") or "gzip" in encoding:
                    payload = gzip.decompress(payload)
                return payload, final_url
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt < attempts:
                time.sleep(attempt * 2)
    raise RuntimeError(f"Unable to fetch {url}: {last_error}")


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def parse_sitemap(payload: bytes) -> tuple[str, list[dict[str, str]]]:
    # Remove a UTF-8 BOM and parse the XML. WordPress/SEO sitemap stylesheets do
    # not affect the underlying sitemap XML.
    payload = payload.lstrip(b"\xef\xbb\xbf\x00\t\r\n ")
    root = ET.fromstring(payload)
    kind = local_name(root.tag)
    entries: list[dict[str, str]] = []
    for child in root:
        child_kind = local_name(child.tag)
        if child_kind not in {"sitemap", "url"}:
            continue
        record: dict[str, str] = {}
        for item in child:
            key = local_name(item.tag)
            text = (item.text or "").strip()
            if key in {"loc", "lastmod"} and text:
                record[key] = text
        if record.get("loc"):
            entries.append(record)
    return kind, entries


def normalize_url(url: str) -> str | None:
    value = url.strip()
    if not value:
        return None
    parsed = urlparse(value)
    host = (parsed.hostname or "").lower()
    if host == f"www.{DOMAIN}":
        host = DOMAIN
    if host != DOMAIN:
        return None
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if any(part in path.lower() for part in EXCLUDED_PATH_PARTS):
        return None
    if parsed.query or parsed.fragment:
        # Sitemaps should contain canonical URLs. Query strings and fragments are
        # excluded to avoid generating duplicate or tracking URLs.
        return None
    lower_path = path.lower()
    if lower_path.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".pdf", ".zip", ".xlsx", ".csv", ".txt")):
        # Keep the two discovery files even though they use an XML-like endpoint.
        return None
    if path != "/" and not path.endswith("/") and "." not in path.rsplit("/", 1)[-1]:
        path += "/"
    return urlunparse(("https", DOMAIN, path, "", "", ""))


def crawl_sitemaps() -> tuple[dict[str, str], list[str], list[str]]:
    urls: dict[str, str] = {normalize_url(u) or u: "" for u in CONFIRMED_SEEDS}
    visited: set[str] = set()
    queue: list[str] = list(SITEMAP_CANDIDATES)
    successful: list[str] = []
    errors: list[str] = []

    while queue:
        sitemap_url = queue.pop(0)
        if sitemap_url in visited:
            continue
        visited.add(sitemap_url)
        try:
            payload, final_url = fetch_bytes(sitemap_url)
            kind, entries = parse_sitemap(payload)
            successful.append(final_url)
        except (RuntimeError, ET.ParseError, ValueError) as exc:
            errors.append(str(exc))
            continue

        if kind == "sitemapindex":
            for entry in entries:
                loc = entry["loc"]
                parsed = urlparse(loc)
                if (parsed.hostname or "").lower().removeprefix("www.") == DOMAIN:
                    queue.append(loc)
        elif kind == "urlset":
            for entry in entries:
                normalized = normalize_url(entry["loc"])
                if normalized:
                    lastmod = entry.get("lastmod", "")
                    if not urls.get(normalized) or lastmod > urls.get(normalized, ""):
                        urls[normalized] = lastmod
        else:
            errors.append(f"Unexpected XML root {kind!r} at {final_url}")

    return urls, sorted(set(successful)), errors


def display_title(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path:
        return "Salar Cafe home"
    if path == "statistical-calculators":
        return "Statistical Calculators Library"
    if path == "ap-score-calculator":
        return "AP Score Calculator Hub"
    if path.endswith(".xml"):
        return path.replace("_", " ").replace("-", " ").title()
    text = path.rsplit("/", 1)[-1].replace("-", " ")
    replacements = {
        "anova": "ANOVA",
        "manova": "MANOVA",
        "mancova": "MANCOVA",
        "ancova": "ANCOVA",
        "spss": "SPSS",
        "python": "Python",
        "excel": "Excel",
        "icc": "ICC",
        "apa": "APA",
        "ap": "AP",
        "r": "R",
        "z": "Z",
        "t": "T",
        "chi": "Chi",
        "square": "Square",
        "kappa": "Kappa",
    }
    words = [replacements.get(word.lower(), word.capitalize()) for word in text.split()]
    title = " ".join(words)
    title = title.replace("Cooks", "Cook’s").replace("Kendalls", "Kendall’s")
    title = title.replace("Welchs", "Welch’s").replace("Fishers", "Fisher’s")
    return title


def classify(url: str) -> str:
    path = urlparse(url).path.lower()
    slug = path.strip("/")
    if not slug:
        return "Main hubs and discovery"
    if slug.endswith(".xml"):
        return "Main hubs and discovery"
    if "/statistical-calculators/" in path:
        return "Statistical calculators"
    if "ap-" in slug and "score-calculator" in slug:
        return "AP score calculators"
    if any(token in slug for token in ("calculator", "solver", "equation-plotter", "dice-counter")):
        return "General calculators and solvers"
    if slug.startswith("ap-statistics") or slug in {
        "introducing-statistics", "categorical-and-quantitative-variables",
        "frequency-and-relative-frequency-tables", "two-way-tables-relative-frequency",
        "percentiles-and-z-scores", "exploring-one-variable-data",
        "scatterplots-and-correlation", "least-squares-regression-line",
        "residuals-in-ap-statistics", "experimental-design", "randomized-experiments",
        "probability-rules", "conditional-probability-and-independence",
    }:
        return "AP Statistics learning resources"
    if any(token in slug for token in (
        "regression", "linear-model", "estimating-equations", "additive-model",
        "hurdle-model", "cox-", "cphm", "failure-time", "r-squared",
    )):
        return "Regression and statistical models"
    if any(token in slug for token in (
        "anova", "manova", "mancova", "ancova", "tukey", "games-howell",
        "dunnett", "bonferroni", "scheffe", "sidak", "newman-keuls",
        "gabriel", "waller-duncan", "tamhane", "pairwise-comparisons",
        "sum-of-squares", "eta-squared", "omega-squared", "cohens-f",
        "simple-effects", "contrast-analysis", "interaction-effects",
    )):
        return "ANOVA, ANCOVA, MANOVA and post-hoc methods"
    if any(token in slug for token in (
        "correlation", "kendalls-tau", "spearman", "cramers-v", "phi-coefficient",
        "biserial", "polychoric", "polyserial", "tetrachoric", "contingency-coefficient",
    )):
        return "Correlation and association"
    if any(token in slug for token in (
        "mann-whitney", "wilcoxon", "kruskal", "friedman", "dunns-test",
        "conover-test", "brunner-munzel", "ansari-bradley", "jonckheere",
        "quade-test", "nemenyi", "van-der-waerden", "runs-test", "savage-scores",
        "siegel", "steel-dwass", "median-test", "moods-median", "fligner-killeen",
        "kolmogorov-smirnov-two-sample", "pages-trend", "nonparametric",
    )):
        return "Nonparametric tests"
    if any(token in slug for token in (
        "reliability", "agreement", "cronbach", "bland-altman", "kappa",
        "item-total", "spearman-brown", "test-retest", "inter-rater", "intra-rater",
    )):
        return "Reliability and agreement"
    if any(token in slug for token in (
        "chi-square", "fishers-exact", "fisher-freeman", "barnards-exact",
        "boschloo", "mcnemar", "mantel-haenszel", "breslow-day", "odds-ratio",
        "relative-risk", "risk-difference", "binomial-test", "categorical-data",
        "cochrans-q", "bowkers", "g-test", "likelihood-ratio",
    )):
        return "Categorical, exact and agreement tests"
    if any(token in slug for token in (
        "t-test", "z-test", "z-interval", "t-interval", "hypothesis",
        "p-value", "type-i-and-type-ii", "confidence-interval",
    )):
        return "T tests, Z tests and statistical inference"
    if any(token in slug for token in (
        "normality", "shapiro", "anderson-darling", "jarque-bera", "lilliefors",
        "breusch-pagan", "white-test", "levene", "bartlett", "cochran-c",
        "hartley", "mahalanobis", "multicollinearity", "variance-inflation",
        "studentized-residual", "transformation", "q-q-plot", "p-p-plot",
        "mauchly", "ramsey-reset", "outlier", "diagnostic",
    )):
        return "Assumptions, diagnostics and transformations"
    if any(token in slug for token in (
        "mean", "median", "mode", "standard-deviation", "standard-error", "variance",
        "z-score", "range", "quartile", "percentile", "skewness", "kurtosis",
        "frequency", "histogram", "box-plot", "normal-distribution", "central-limit",
        "effect-size", "statistical-power", "descriptive-statistics", "probability",
        "sampling", "random-variable", "binomial-distribution", "geometric-distribution",
    )):
        return "Statistical foundations and probability"
    if path.startswith("/category/") or path.startswith("/tag/"):
        return "Public archive pages"
    return "Other Salar Cafe resources"


def write_outputs(urls: dict[str, str], sitemaps: list[str], errors: list[str]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    records = [
        {
            "title": display_title(url),
            "url": url,
            "category": classify(url),
            "last_modified": lastmod,
        }
        for url, lastmod in urls.items()
    ]
    records.sort(key=lambda row: (row["category"].casefold(), row["title"].casefold(), row["url"]))

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["category", "title", "url", "last_modified"])
        writer.writeheader()
        writer.writerows(records)

    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    JSON_PATH.write_text(
        json.dumps(
            {
                "website": BASE,
                "generated_utc": generated,
                "url_count": len(records),
                "sitemaps_read": sitemaps,
                "warnings": errors,
                "urls": records,
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for record in records:
        grouped[record["category"]].append(record)

    category_order = [
        "Main hubs and discovery",
        "Statistical foundations and probability",
        "T tests, Z tests and statistical inference",
        "Assumptions, diagnostics and transformations",
        "ANOVA, ANCOVA, MANOVA and post-hoc methods",
        "Regression and statistical models",
        "Correlation and association",
        "Categorical, exact and agreement tests",
        "Nonparametric tests",
        "Reliability and agreement",
        "AP Statistics learning resources",
        "Statistical calculators",
        "AP score calculators",
        "General calculators and solvers",
        "Public archive pages",
        "Other Salar Cafe resources",
    ]
    remaining = [name for name in sorted(grouped) if name not in category_order]

    lines = [
        "# Complete Salar Cafe Website Directory",
        "",
        f"**Public URLs cataloged: {len(records):,}**  ",
        f"**Generated automatically: {generated}**",
        "",
        "This directory is generated from the public XML sitemap families of "
        "[Salar Cafe](https://onlineinternetcafe.com/). It is designed to cover the complete "
        "indexable website rather than a small hand-selected group of pages. New public URLs "
        "are added automatically when the website sitemap is refreshed.",
        "",
        "## Source sitemaps",
        "",
    ]
    for sitemap in sitemaps or SITEMAP_CANDIDATES:
        lines.append(f"- [{sitemap}]({sitemap})")
    lines.extend([
        "",
        "## Machine-readable files",
        "",
        "- [All public URLs as CSV](data/all-public-urls.csv)",
        "- [All public URLs as JSON](data/all-public-urls.json)",
        "",
        "## Category summary",
        "",
        "| Category | URLs |",
        "|---|---:|",
    ])
    for category in category_order + remaining:
        if category in grouped:
            anchor = re.sub(r"[^a-z0-9 -]", "", category.lower()).replace(" ", "-")
            lines.append(f"| [{category}](#{anchor}) | {len(grouped[category]):,} |")

    for category in category_order + remaining:
        items = grouped.get(category)
        if not items:
            continue
        lines.extend(["", f"## {category}", ""])
        for item in items:
            suffix = f" — last modified {item['last_modified']}" if item["last_modified"] else ""
            lines.append(f"- [{item['title']}]({item['url']}){suffix}")

    if errors:
        lines.extend([
            "",
            "## Refresh warnings",
            "",
            "The directory retained confirmed seed URLs when one or more sitemap endpoints could not be read. "
            "The next scheduled run will try those endpoints again.",
            "",
        ])
        for error in errors:
            lines.append(f"- `{error}`")

    lines.extend([
        "",
        "---",
        "",
        "Maintained by Salar Cafe. The website itself remains the canonical source for page content, "
        "titles, formulas, calculators, datasets, and publication status.",
        "",
    ])
    MARKDOWN_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    urls, sitemaps, errors = crawl_sitemaps()
    write_outputs(urls, sitemaps, errors)
    print(f"Cataloged {len(urls):,} public URLs from {len(sitemaps)} sitemap endpoints.")
    if errors:
        print(f"Warnings: {len(errors)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
