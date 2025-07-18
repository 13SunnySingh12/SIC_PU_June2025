import pandas as pd

def read_excel_file1():
    
    file_path = 'C:\LEARNING\SIC_PU_June2025\week_4\Pandas\Datasets\data.csv'
    df = pd.read_csv(file_path)

    for row in df.iterrows():              # same generator, unpacked differently
        print(row[1][0], row[1][1])        # row[1] is the Series; [0] & [1] pick cols

read_excel_file1()
