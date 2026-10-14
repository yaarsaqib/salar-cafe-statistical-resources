"""Offline tests for the bounded read-only monitor. No live requests."""
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "dags"))
import site_monitor_lib as monitor


class MetadataTests(unittest.TestCase):
    def test_html_parser(self):
        page = monitor.PageMetadata()
        page.feed('<html><head><title>Sample</title>'
                  '<meta name="description" content="Text">'
                  '<meta name="robots" content="index, follow">'
                  '<link rel="canonical" href="https://onlineinternetcafe.com/test/">'
                  '</head><body><h1>Only one</h1></body></html>')
        self.assertEqual(page.title, "Sample")
        self.assertEqual(page.h1_count, 1)
        self.assertEqual(page.description, "Text")
        self.assertEqual(page.canonical, "https://onlineinternetcafe.com/test/")

    def test_host_restriction(self):
        self.assertTrue(monitor.valid_site_url("https://onlineinternetcafe.com/stats/"))
        for bad in ("https://evil.example/", "https://onlineinternetcafe.com.evil.example/",
                    "http://onlineinternetcafe.com/", "https://onlineinternetcafe.com/?x=1",
                    "https://onlineinternetcafe.com/report.pdf"):
            self.assertFalse(monitor.valid_site_url(bad))

    def test_fixed_batch_coverage(self):
        urls = [f"https://onlineinternetcafe.com/page-{i}/" for i in range(23)]
        days = [date(2026, 10, 15), date(2026, 10, 16), date(2026, 10, 17)]
        batches = [monitor.select_pages(urls, day, batch_size=10)[0] for day in days]
        self.assertEqual(len(set.union(*(set(part) for part in batches))), len(urls))
        self.assertEqual(sum(len(part) for part in batches), len(urls))

    def test_report_output_and_counts(self):
        with tempfile.TemporaryDirectory() as root:
            catalog = Path(root) / "catalog.json"
            report_dir = Path(root) / "reports"
            catalog.write_text(json.dumps({
                "website": monitor.SITE, "generated_utc": "2026-10-15",
                "urls": [{"url": monitor.SITE + "/"}]
            }), encoding="utf-8")
            fake_page = {"url": monitor.SITE + "/", "status": 200, "issues": [],
                         "elapsed_ms": 12, "bytes_read": 20}
            with patch.object(monitor, "CATALOG_PATH", catalog), \
                 patch.object(monitor, "check_page", return_value=fake_page), \
                 patch.object(monitor, "get_wordpress_counts", return_value={"pages": 2525, "posts": 5}), \
                 patch.object(monitor, "get_ga4_metrics", return_value={"status": "not_configured"}):
                result = monitor.run(date(2026, 10, 15), batch_size=10, delay=0,
                                     output_dir=report_dir)
            self.assertEqual(result["http_200"], 1)
            self.assertTrue((report_dir / "latest.md").exists())
            snapshot = json.loads((report_dir / "latest.json").read_text(encoding="utf-8"))
            self.assertEqual(snapshot["catalog_url_count"], 1)
            self.assertEqual(snapshot["wordpress"]["pages"], 2525)


if __name__ == "__main__":
    unittest.main()
