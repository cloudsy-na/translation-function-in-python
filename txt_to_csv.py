import pandas as pd

df=pd.read_table('exam_text.txt',header=None)
print(df)

output=df.to_csv('coba.csv')
