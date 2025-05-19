#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:28:05 2025

@author: argelio

Permite organizar los archivos según su extesión, crea subcarpeta y se queda en observador.
"""

import shutil
from pathlib import Path
from datetime import datetime
import os
from tkinter import Tk, filedialog

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
   
    
    # se valida la ruta de las carpeta
    for carpeta in carpetas:
        ruta_carpeta=os.path.join(ruta, carpeta)
       
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
        
        contador=0 # para controlar si hubo archivo en en el directorio
        
        #obtener ruta absoluta
        directorio=os.path.abspath(directorio)
        
        #crear carpeta de organización
        carpetas=Crear_Organizar_Carpeta(directorio)
               
      
        log_filename=os.path.join(directorio,"log_organizacion.txt")
           
        
        for archivo in os.listdir(directorio):
            ruta_archivos=os.path.join(directorio, archivo)
            
                
            #ignorar carpetas y archivos ocultos
            if os.path.isfile(ruta_archivos) and not ruta_archivos.startswith('.') and ruta_archivos != log_filename :
                #obtener extesion
                extension=os.path.splitext(archivo)[1] # archivo.pdf lo que hace es separar |archivo|pdf|
                
                #obneter la fecha de ultima modificacion del archivo
                fecha_modificacion=datetime.fromtimestamp(os.path.getmtime(ruta_archivos))
                nombre_subcarpeta=fecha_modificacion.strftime('%Y-%m')#formatea a "2025-05"
                print(fecha_modificacion)       
                
                
                #determinar carpeta destino
                carpeta_destino=obtener_carpeta_por_extension(extension,carpetas)
                ruta_subcarpeta=os.path.join(directorio, carpeta_destino,nombre_subcarpeta)
                
                print(ruta_subcarpeta)
                
                if not os.path.exists(ruta_subcarpeta):
                    os.makedirs(ruta_subcarpeta)
                
                destino_carpeta=os.path.join(ruta_subcarpeta,archivo)             
                   
         
                #mover archivos
                try:
                    shutil.move(ruta_archivos, destino_carpeta)
                    with open(log_filename, 'a', encoding='utf-8') as log_file:
                        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Movido: {archivo} --> {destino_carpeta}/\n ")
                        contador+=1
                except Exception as e:
                    print(f' error al mover  {archivo}:{str(e)}')                
                  
                
        if contador < 1:
            print("No se encontraron archivos para organizar")
            with open(log_filename, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - no se encontraron archivos para organizar en {directorio}/\n ")              
            
                
    except Exception as e:
        print(f"Error durante la organización: {str(e)}")        
        

        
ventana=Tk()
ventana.withdraw()# para evitar que aparezca la venta de shell o simbolo del sistema (sistema operativo windows)

ruta=filedialog.askdirectory(title="Seleccine la carpeta a ordener")# permite seleccionar la ruta del directorio

#Crear_Organizar_Carpeta(ruta)
organizar_archivos(ruta)
print('proceso finalizado consulte el log')