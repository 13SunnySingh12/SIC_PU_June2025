"""Loop over DataFrame rows with iterrows() and print the first two columns."""

from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "data.csv"


def print_first_two_columns():
    df = pd.read_csv(DATA_FILE)

    for index, row in df.iterrows():        # row-wise generator
        # .iloc selects by position; row[0] would index by label.
        print(row.iloc[0], "  ", row.iloc[1])


if __name__ == "__main__":
    print_first_two_columns()
