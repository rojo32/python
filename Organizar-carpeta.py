#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:28:05 2025

@author: argelio
"""
import shutil
from pathlib import Path
from datetime import datetime
import os

def Crear_Organizar_Carpeta(ruta):
    """se crea las carpetas para organizar los archivos"""
    carpetas={
        'imagenes':['.jpg','.jpeg','.png','.gif','.bmp'],
        'documentos':['.doc','.docx','.pdf','.txt'],
        'datasets':['.xls','.csv','.sav'],
        'audio':['.mp3','.wav','flac','ma4'],
        'video':['.mp4','.avi','.mkv','.mov'],
        'comprimidos':['.zip','.rar','.7z'],
        'otros':[]
        }
    print(carpetas)
    
    # se valida la ruta de las carpeta
    for carpeta in carpetas:
        ruta_carpeta=os.path.join(ruta, carpeta)
        print(f'ruta carpta {ruta_carpeta}')
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            print(f'se crea la ruta sino existe{ruta_carpeta}')
    
    return carpetas
        
def obtener_carpeta_por_extension(extension, diccionario_carpeta):
    #segun la extesion determina la carpeta del archivo
    for carpeta, extensiones in diccionario_carpeta.items():
        if extension.lower() in extensiones:
            return carpeta
        
    return 'otros'

def organizar_archivos(directorio):
    #organiza los archivos en la carpeta
    try:
        #Crear el registro de movimiento
        log=[]
        
        #obtener ruta absoluta
        directorio=os.path.abspath(directorio)
        print(f'el directorio es {directorio}')
        
        #crear carpeta de organización
        carpetas=Crear_Organizar_Carpeta(directorio)
        print(f'se crea la carpeta {carpetas}')
        
        #recorrer archivos en el directorio
        
        for archivo in os.listdir(directorio):
            ruta_archivos=os.path.join(directorio, archivo)
            
            #ignorar carpetas y archivos ocultos
            if os.path.isfile(ruta_archivos) and not ruta_archivos.startswith('.'):
                #obtener extesion
                extension=os.path.splitext(archivo)[1] # archivo.pdf lo que hace es separar |archivo|pdf|
                
                #determinar carpeta destino
                carpeta_destino=obtener_carpeta_por_extension(extension,carpetas)
                destino_carpeta=os.path.join(directorio, carpeta_destino,archivo)
                
                #mover archivos
                try:
                    shutil.move(ruta_archivos, destino_carpeta)
                    log.append(f'movido {archivo}-->{destino_carpeta}/')
                except Exception as e:
                    log.append(f' error al mover  {archivo}:{str(e)}')
        #generar log
        if log:
            print("\n== reporte de organización===")
            print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Directorio: {directorio}")
            print("\Movimientos realizados")
            for entrar in log:
                print(f"-{entrar}")
        else:
            print("No se encontraron archivos para organizar")
            
    except Exception as e:
        print(f"Error durante la organización: {str(e)}")
        
if __name__=="__main__":
    #solicitar directorio a organizar
    directorio=input("Ingrese la ruta del directorio a organizar (Enter para directorio actual) ")
    
    #Si no se especifica directorio, usar el actual
    if not directorio:
        directorio="."
        
    #verificar que el directorio existe
    if not os.path.exists(directorio):
        print("Error: El directorio especificado no existe.")
        exit(1)
        
    #confirmar acción
    print(f'\nSe organizaran los archivos en: {os.path.abspath(directorio)}')
    confirmacion=input("¿Desea continuar? (S/N):")
    if confirmacion.lower():
        organizar_archivos(directorio)
        
    
            
            
                    
            
        
    
        
            
    
    
