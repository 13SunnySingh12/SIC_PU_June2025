"""What is this written for?

Walking a DataFrame row by row with `DataFrame.iterrows()`, which yields an
(index, Series) pair per row. Here the index is unpacked separately and the
first two columns of each row are printed by position.
"""

from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "data.csv"


def print_first_two_columns():
    df = pd.read_csv(DATA_FILE)

    for index, row in df.iterrows():        # row-wise generator
        # .iloc selects by position; plain row[0] indexes by label and no
        # longer falls back to position in current pandas.
        print(row.iloc[0], "  ", row.iloc[1])


if __name__ == "__main__":
    print_first_two_columns()
