# Salar Cafe — Apache Airflow daily monitoring

Target: https://onlineinternetcafe.com

This folder implements a read-only daily health pipeline using
[Apache Airflow](https://github.com/apache/airflow). The shared Python
monitor also runs in GitHub Actions, so the first daily reports can operate
without installing Airflow or Python on the WordPress host.

## Collection and analytics

- Rotating audits of public pages from the existing data/all-public-urls.json catalog
- Status codes, request durations, title, H1 count, description, canonical and robots/noindex
- Public WordPress page and post counts
- Optional Google Analytics 4 aggregate sessions, active users and page views
- Dated Markdown/JSON snapshots with individual URLs needing human review

The URL catalog is populated by the existing full-site-directory workflow.
The monitor uses fixed batches of 120 rotating URLs/day plus five priority
URLs (as available). For roughly 3,268 URLs, a rotation needs about 28 days.
No guessed organic traffic, rankings, visitor counts or Search Console data.

## Daily GitHub Actions execution

Workflow: .github/workflows/salar-cafe-daily-monitor.yml

Scheduled for 03:15 UTC daily (08:15 Asia/Karachi).
Manual execution: GitHub repository -> Actions -> Salar Cafe daily health report -> Run workflow.

Results are saved to reports/airflow/YYYY-MM-DD.json, YYYY-MM-DD.md,
latest.json and latest.md; the workflow also uploads a downloadable artifact.
Actions must be enabled and workflow contents:write permission granted for
automatic commits. If branch protection prohibits pushing reports, Actions
artifacts remain an alternative.

## Run the same monitor manually

Requires Python 3.10+ and a working checkout of this repository.

~~~bash
python -m unittest discover -s airflow/tests -v
python airflow/dags/site_monitor_lib.py --batch-size 25
~~~

Options: --date 2026-10-15 for a particular day; --delay 0.25 to pace requests.

## Deploy on Apache Airflow 3

Airflow is a Python scheduler requiring a persistent server. It is not a
normal WordPress plugin and cannot simply be activated on shared hosting.
Use a VPS or managed Airflow installation and follow the
[official Docker guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
Official demo Docker Compose is not production hardened. Production requires
appropriate isolation, authentication, PostgreSQL, secrets and backups.

Mount these repository directories into the Airflow scheduler, DAG processor
and worker containers (the worker needs write access to reports):

| Repository directory | Container directory | Mode |
| --- | --- | --- |
| ./airflow/dags | /opt/airflow/dags | read-only |
| ./data | /opt/data | read-only |
| ./reports | /opt/reports | read-write |

The module resolves the repository data path as /opt/data when mounted above.
The DAG ID is salar_cafe_daily_site_health, running 03:15 UTC. Optionally set
SALAR_BATCH_SIZE on the worker to an integer from 1 to 300.

Do not allow GitHub Actions and Airflow to write to the same shared report
storage concurrently. Keep separate storage or disable one of the schedulers.

## Optional GA4 traffic integration

The monitor deliberately reports GA4 as not_configured until authorized data
access is provided. Create a read-only service account with GA4 property access.
Install the google-analytics-data Python library inside the Airflow worker.

Airflow environment:
- GA4_PROPERTY_ID: numeric GA4 property ID
- GOOGLE_APPLICATION_CREDENTIALS: private absolute path of service account JSON

GitHub Actions repository secrets:
- GA4_PROPERTY_ID: numeric GA4 property ID
- GA4_SERVICE_ACCOUNT_JSON_B64: base64-encoded full service account JSON

The workflow decodes the secret into a temporary private runner file.
Never commit this JSON, WordPress passwords, personally identifiable
analytics data or user-uploaded statistics files.

## Scope and limitations

This is a public HTTP/HTML monitor, not a JavaScript browser test or a
calculator-formula verification framework. Heuristic SEO flags require human
review. Each daily batch samples a subset, not the entire catalog. Live
execution is only confirmed after a successful Actions run or after deploying
the separate Airflow runtime.
