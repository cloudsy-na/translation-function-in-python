import pandas as pd
import ctypes

df1 = pd.read_csv('C:\\Users\\andriawan\\Documents\\2022\\Python\\Latihan_2\\test_filter\\database_pim.csv')
#print(df1)

df2 = pd.read_csv('C:\\Users\\andriawan\\Documents\\2022\\Python\\Latihan_2\\test_filter\\new_data.csv')
#print(df2)

database = pd.DataFrame(df1)
newData = pd.DataFrame(df2)
Result = pd.merge(df1,df2,on='pg_name',how='inner')
#print(Result)
#print(Result[['pg_name', 'pg_name_bahasa']])
Result.to_csv("result_trans_inner.csv")

database = pd.DataFrame(df1)
newData = pd.DataFrame(df2)
Result = pd.merge(df1,df2,on='pg_name',how='right')
#print(Result)
#print(Result[['pg_name', 'pg_name_bahasa']])
Result.to_csv("result_trans_right.csv")

df_r = pd.read_csv("C:\\Users\\andriawan\\Documents\\2022\\Python\\Latihan_2\\test_filter\\result_trans_right.csv")
#print(df_r)

df1=pd.DataFrame(df_r,columns=['pg_code', 'pg_name', 'pg_bahasa'])
# print(df1)

rslt_f = df1.loc[df1['pg_bahasa'].isna()]   
hasil=(rslt_f['pg_name'])

hasil.to_csv('contoh hasil Nan.csv')
