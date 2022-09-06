import pandas as pd
import googletrans
from googletrans import Translator, LANGUAGES
import ctypes

df = pd.read_csv ("C:\\Users\\andriawan\\Documents\\2022\\Python\Latihan_2\\translate\\bq-results-re003.csv")
#print(df.head(5))

translator = Translator()
translations = {}
for column in df.columns:
    # Unique elements of the column
    unique_elements = df['pg_name'].unique()
    for element in unique_elements:
        # Adding all the translations to a dictionary (translations)
        translations[element] = translator.translate(element, dest='id').text 
#print(translations)

df_trans = df.replace(translations, inplace = True)
#print(df.head(20))

#df.to_excel("filename_here.xlsx")
df.to_csv("bq-results-re005_output.csv")

ctypes.windll.user32.MessageBoxW(0, "Selamat Bro, Berhasil !","Sekilas Info", 0)
