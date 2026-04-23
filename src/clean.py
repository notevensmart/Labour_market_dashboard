import pandas as pd
from src.config import RAW_DATA_PATH, CLEAN_DATA_PATH


def clean_data(df):
    df = df.copy()
    df.columns = [col.lower().strip() for col in df.columns]
    df = df.dropna()
    return df


def main():
    df = pd.read_csv(RAW_DATA_PATH)
    df_clean = clean_data(df)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)
    print("Cleaned data saved")


if __name__ == "__main__":
    main()
