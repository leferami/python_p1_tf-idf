from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer
import re
import codecs
codecs.BOM_UTF8
'\xef\xbb\xbf'


palabrasImportantes =[]
palabrasSteming = []
with codecs.open("archivo.txt", "r", encoding="utf-8-sig") as f:
    for linea in f:
        linea = linea[:-1].split(" ")
        print "linea:",linea
        for palabra in linea:
            palabra = re.sub('[\!@#$%^&*-/,.;:]','',palabra)
            print "palabra:",palabra



#print palabrasImportantes