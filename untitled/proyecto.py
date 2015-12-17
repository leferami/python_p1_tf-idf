from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer
import codecs
codecs.BOM_UTF8
'\xef\xbb\xbf'

stemmer = SnowballStemmer("spanish")
i = 0
repetidas = 0
archivo = open("archivo.txt", "r")
palabrasImportantes =[]
palabrasSteming = []
for i in archivo.readlines():
   linea = i[:-1].split(" ")
   print linea
   #palabras = re.sub('[\!@#$%^&*-/,.;:]','',palabras)
   #print linea
   for palabra in linea:
       #print palabra
       palabra = re.sub('[\!@#$%^&*-/,.;:]','',palabra)
       palabra.lower()
       if palabra not in stopwords.words('spanish'):
           palabrasImportantes.append(palabra)
print palabrasImportantes
#palabrasSteming = [stemmer.stem(plural) for plural in palabrasImportantes]
#print palabrasSteming
