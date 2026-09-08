import pandas as pd

df1 = pd.read_csv('data/Heart.csv')

def age():
    df2 = df1[df1["age"] > 50]
    return df2