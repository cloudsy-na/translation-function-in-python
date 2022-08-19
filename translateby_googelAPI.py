#you must install the library first
#python m- pip install googletrans

from googletrans import Translator, LANGUAGES

translator = Translator()
text = input("Input Text : ")
transTo = input("Translated to : ")  
hasil = translator.translate(text, dest = transTo)

print("From ", LANGUAGES[hasil.src], " : ", text)
print("To ", LANGUAGES[hasil.dest], " : ", hasil.text)
