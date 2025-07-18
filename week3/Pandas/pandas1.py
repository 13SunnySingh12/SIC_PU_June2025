import pandas as pd

def read_excel_file():

    file_path = "C:\LEARNING\SIC_PU_June2025\week_4\Pandas\Datasets\data.csv"
    df = pd.read_csv(file_path)

    print(df.count())                      # number of non‑NA values in every column
    print(df.head())                       # first 5 rows (default) 
    print(df.tail())                       # last 5 row

read_excel_file()                     