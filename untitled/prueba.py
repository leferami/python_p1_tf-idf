# -*- encoding: utf-8 -*-
from nltk.stem.porter import *
import unicodedata
from nltk.stem.snowball import SnowballStemmer

#menu
def menu():
    print("leer documento .txt o .csv")


######### MAIN PROGRAM ##############
menu()
stemmer = SnowballStemmer("spanish")
array = []
plurals = ['tora','torax','torcer','toreado','toreados','toreandolo','torear','toreara','torearlo','toreo','torero','toreros'
    ,'torio','tormenta','tormentas','tornado','tornados','tornar','tornen','torneo','torneos'];

print(" ".join(SnowballStemmer.languages))
singles = [stemmer.stem(plural) for plural in plurals]

print(' '.join(singles))
singles = ' '.join(singles)
print singles

#def elimina_tildes(self, cadena):
#    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
#   return s.decode()