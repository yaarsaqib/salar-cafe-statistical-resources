"""Salar Cafe production-site read-only health reporting DAG (Apache Airflow 3)."""
from __future__ import annotations

from datetime import datetime, timezone

from airflow.sdk import dag, task

from site_monitor_lib import run


@dag(
    dag_id="salar_cafe_daily_site_health",
    description="Daily rotating website QA, public content counts, optional GA4 and stored reports.",
    schedule="15 3 * * *",
    start_date=datetime(2026, 10, 15, tzinfo=timezone.utc),
    catchup=False,
    max_active_runs=1,
    tags=["salar-cafe", "website-health", "read-only"],
)
def salar_cafe_daily_site_health():
    @task(retries=2)
    def generate_report():
        # Airflow automatically logs task results. No data is published to WordPress.
        return run()

    generate_report()


salar_cafe_daily_site_health()
