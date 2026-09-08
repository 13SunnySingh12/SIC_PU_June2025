"""What is this written for?

Loading a CSV into a pandas DataFrame and taking a first look at it: how many
non-null values each column holds, and the rows at the top and bottom of the
frame. This is the standard first step before any analysis.
"""

from pathlib import Path

import pandas as pd

# Resolved from this file's location, so the script runs from any directory.
DATA_FILE = Path(__file__).parent / "data" / "data.csv"


def summarise_csv():
    df = pd.read_csv(DATA_FILE)

    print(df.count())   # number of non-NA values in every column
    print(df.head())    # first 5 rows
    print(df.tail())    # last 5 rows


if __name__ == "__main__":
    summarise_csv()
