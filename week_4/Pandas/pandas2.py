import pandas as pd

def read_excel_file1():
    
    file_path = 'C:\LEARNING\SIC_PU_June2025\week_4\Pandas\Datasets\data.csv'
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():       # row‑wise generator
        print(row[0], '  ', row[1])        # print 1st & 2nd column values

read_excel_file1()