import pandas as pd
from src.config import RAW_DATA_PATH


def main():
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        print("Data loaded successfully")
        print(df.head())
    except FileNotFoundError:
        print("Raw data file not found. Place your CSV in data/raw/")


if __name__ == "__main__":
    main()
