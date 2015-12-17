# -*- encoding: utf-8 -*-
from __future__ import print_function
import os
def crearArchivo(archivo):
    nombreArchivo = "C:/archivosLenguajesEscritorio/"+archivo
    archi = open(nombreArchivo,'w')
    archivoOut = open("C:/archivosLenguajesUsb/"+archivo,"r")
    copiarArvhivos(archi,archivoOut)

def copiarArvhivos(archi,archivoOut):
    for linea in archivoOut.readlines():
        print(linea)
        archi.write(linea)
    archi.close()

for archivo in os.listdir("C:/archivosLenguajesUsb"):
    if archivo.endswith(".txt"):
        crearArchivo(archivo)
    if archivo.endswith(".csv"):
        print(archivo)
        crearArchivo(archivo)