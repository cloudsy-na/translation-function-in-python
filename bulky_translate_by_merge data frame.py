import pandas as pd
import ctypes

df1 = pd.read_csv('C:\\Users\\andriawan\\Documents\\2022\\Python\\Latihan_2\\dataframe\\database_pim.csv')
#print(df1)

df2 = pd.read_csv('C:\\Users\\andriawan\\Documents\\2022\\Python\\Latihan_2\\dataframe\\new_data.csv')
#print(df2)

database = pd.DataFrame(df1)
newData = pd.DataFrame(df2)
Result = pd.merge(df1,df2,on='pg_name',how='right')
#print(Result)
#print(Result[['pg_name', 'pg_name_bahasa']])
Result.to_csv("result_trans_mergeDF.csv")

ctypes.windll.user32.MessageBoxW(0, "Exported !","Skelebet Info", 0)
