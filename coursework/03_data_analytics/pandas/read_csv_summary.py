"""Read a CSV and print its non-null counts and first and last rows."""

from pathlib import Path

import pandas as pd

# Relative to this file, so the script runs from any directory.
DATA_FILE = Path(__file__).parent / "data" / "data.csv"


def summarise_csv():
    df = pd.read_csv(DATA_FILE)

    print(df.count())   # number of non-NA values in every column
    print(df.head())    # first 5 rows
    print(df.tail())    # last 5 rows


if __name__ == "__main__":
    summarise_csv()
