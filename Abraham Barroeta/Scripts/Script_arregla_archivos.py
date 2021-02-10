import os
import glob
import shutil

#Este es un Script que Organiza los archivos por extension, crea carpetas y copia los archivos alli.



lista_archivos = glob.glob('*') #Se ubican todos los archivos, es similar al comando de buscar de windows

lista_iterable_extensiones = set()
lista_iterable_2 = set()

#Añadiendo cada tipo de archivo a la lista de archivos

for archivo in lista_archivos:
    extension_archivo = archivo.rsplit(sep='.')
    try:
        lista_iterable_extensiones.add(extension_archivo[1])
    except IndexError:
        continue

#Funcion para crear las carpetas

def crear_carpetas():
    for directorio in lista_iterable_extensiones:
        try:
            os.makedirs(directorio + "_archivos")
        except FileExistsError:
            continue

#Funcion para copiar los archivos!

def copiar_a_carpetas():
    for file in lista_archivos:
        fextension = file.split(sep='.')
        try:
            shutil.copy(file, fextension[1]+"_archivos")
        except (OSError, IndexError):
            continue
    

crear_carpetas()
copiar_a_carpetas()

