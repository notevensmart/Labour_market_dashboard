# Labour Market Dashboard

A lightweight public-sector style analytics project using Australian labour market data.

This repository includes:
- a Python data pipeline for ingesting, cleaning, validating, and analysing labour market data
- a Streamlit dashboard for interactive exploration
- Power BI-ready exports for presentation and reporting
- a small automated test suite for core cleaning logic

## Project goal

This project is designed to demonstrate the kind of end-to-end workflow valued in APS-style data analyst roles:
- ingest raw data
- clean and standardise it
- calculate useful labour market indicators
- export dashboard-ready tables
- communicate insights through a simple dashboard

## Recommended dataset

Use a CSV from the Australian Bureau of Statistics (ABS) Labour Force series.

Place the raw file here:

`data/raw/labour_force.csv`

The cleaning pipeline expects a tidy or near-tidy CSV with columns that can be mapped to:
- date
- state
- unemployment_rate
- participation_rate
- employment_to_population_ratio

If your source uses different names, adjust `src/config.py`.

## Repository structure

```text
Labour_market_dashboard/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── exports/
│   └── powerbi/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── ingest.py
│   ├── clean.py
│   ├── analyse.py
│   ├── export_sqlite.py
│   └── export_powerbi.py
├── app/
│   └── dashboard.py
└── tests/
    └── test_clean.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Run pipeline

```bash
python -m src.ingest
python -m src.clean
python -m src.analyse
python -m src.export_sqlite
python -m src.export_powerbi
```

## Run dashboard

```bash
streamlit run app/dashboard.py
```

## Output files

The pipeline writes:
- `data/processed/labour_market_clean.csv`
- `data/processed/labour_market_summary.csv`
- `exports/powerbi/labour_market_dashboard_table.csv`
- `exports/powerbi/labour_market.db`

## Suggested Power BI visuals

Use `exports/powerbi/labour_market_dashboard_table.csv` or the SQLite database to build:
- a KPI card for latest national average unemployment rate
- a line chart of unemployment rate over time by state
- a line chart of participation rate over time
- a bar chart comparing latest unemployment rate across states
- slicers for state and date

## Resume framing

Example bullet:

- Built a public-sector labour market analytics dashboard using Python and Australian labour force data, transforming raw datasets into stakeholder-friendly insights on unemployment and participation trends.

## Notes

This project is intentionally simple and practical. It is designed to show data cleaning, analysis, documentation, and dashboard-readiness rather than unnecessary complexity.
