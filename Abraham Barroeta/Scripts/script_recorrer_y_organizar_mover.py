#Este Script lo que hace es mover los archivos a una carpeta cuyo nombre es la extension de los archivos.

'''
    Este script debe copiarse en la carpeta donde se desee organizar todo para su correcto funcionamiento.
    
'''

import os
import glob
import shutil

#Esto es basicamente para obtener la ruta de la carpeta donde 
#se esta ejecutando el script
ruta = os.getcwd()

print('-------------------------------------------------')
print('La ruta de la carpeta donde esta el script es: '+ ruta)
print('-------------------------------------------------')

#Esta funcion crea una lista de archivos pasandoles una ruta
def crear_lista_archivos(ruta_1):
    '''
        Esta funcion retorna una lista de archivos de la ruta que se ingrese
    '''
    lista_archivos = set()
    for nombres in glob.glob(str(ruta_1)+'/*'):
        lista_archivos.add(nombres)
    return lista_archivos

def obtener_extensiones(lista_para_division):
    '''
            Esta funcion retorna las extension de una determinada lista
        de archivos que se le asignen
    '''
    lista_de_extensiones = set()
    for archivos in lista_para_division:
        extension_archivos = archivos.rsplit(sep='.')
        
        try:
            lista_de_extensiones.add(extension_archivos[1])
        except IndexError:
            continue
    return lista_de_extensiones

def crear_carpetas(directorio_padre,lista_entrada):
    '''
        Crea carpetas en funcion a una lista que se le asigne con 
        la terminacion "_files"
    '''

    for folder in lista_entrada:
        try:
            folder_to_create_1 = folder + '_files'
            ruta_final  = os.path.join(directorio_padre,folder_to_create_1)
            os.makedirs(ruta_final)
        except (OSError, IndexError):
            continue

def mover_a_carpetas(entrante_lista_archivos, entrante_ruta_padre):
    for files in entrante_lista_archivos:
        fextension = files.rsplit(sep='.')
        try:
            ruta_destino =os.path.join(entrante_ruta_padre,fextension[1]+"_files", "") 
            print('///////////////////////')
            print(files)
            print(ruta_destino)
            print('//////////////////////////')
            shutil.move(files,ruta_destino)
        except (OSError, IndexError):
            continue

#Recorrer las carpetas 

for (root, folders, files) in os.walk(ruta):
    var1 = crear_lista_archivos(root)
    var2 = obtener_extensiones(var1)
    crear_carpetas(root, var2)
    mover_a_carpetas(var1, root)

    
    











    

