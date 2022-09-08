import pandas as pd

df=pd.read_table('exam_text.txt',header=None)
df.columns=["product name"]
print(df)

output=df.to_csv('coba.csv')
