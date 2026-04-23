RAW_DATA_PATH = "data/raw/labour_force.csv"
CLEAN_DATA_PATH = "data/processed/labour_market_clean.csv"
SUMMARY_DATA_PATH = "data/processed/labour_market_summary.csv"
POWERBI_EXPORT_PATH = "exports/powerbi/labour_market_dashboard_table.csv"
SQLITE_DB_PATH = "exports/powerbi/labour_market.db"

COLUMN_MAPPING = {
    "date": "date",
    "state": "state",
    "unemployment_rate": "unemployment_rate",
    "participation_rate": "participation_rate",
    "employment_to_population_ratio": "employment_to_population_ratio"
}
