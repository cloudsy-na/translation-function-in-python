import pandas as pd

df_r = pd.read_csv("C:\\Users\\andriawan\\Documents\\2022\\Python\\Latihan_2\\test_filter\\result_trans.csv")
#print(df_r)

df1=pd.DataFrame(df_r,columns=['pg_code', 'pg_name', 'pg_bahasa'])
# print(df1)

rslt_f = df1.loc[df1['pg_bahasa'].isna()]   
hasil=(rslt_f['pg_name'])

hasil.to_csv('contoh hasil Nan.csv')
