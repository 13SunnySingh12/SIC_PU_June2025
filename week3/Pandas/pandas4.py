import pandas as pd

data = {
    "Name": ["Sumeeth", "Sunil", "Suresh"],
    "Branch": ["Btech", "Mtech", "Phd"],
    "Marks": [85.5, 98.5, 80.5]
}

df = pd.DataFrame(data)
print(df)

df = df.to_csv()
print(df)
