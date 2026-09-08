"""What is this written for?

The same `iterrows()` walk as iterate_rows_iterrows.py, but keeping each
(index, Series) pair as a single tuple instead of unpacking it. It shows that
`row[1]` is the Series holding the actual row data, which is then indexed by
position.
"""

from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "data.csv"


def print_first_two_columns():
    df = pd.read_csv(DATA_FILE)

    for row in df.iterrows():               # same generator, unpacked differently
        series = row[1]                     # row[0] is the index, row[1] the data
        print(series.iloc[0], series.iloc[1])


if __name__ == "__main__":
    print_first_two_columns()
