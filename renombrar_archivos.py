import os
import tkinter as tk
from tkinter import Tk, filedialog,Label,messagebox

extesiones=".jpg"
prefijo="imagen_"

def seleccionar_carpeta():
    ruta=filedialog.askdirectory(title="Seleccine la carpeta a ordener")# permite seleccionar la ruta del directorio
    entrada_carpeta.insert(0,ruta)
    
def renombrar_archivos():
    
    carpeta=entrada_carpeta.get()
    prefijo=entra_prefijo.get()
    extesiones=tuple(entra_extesiones.get().split(','))#split devuelve la lista, con la funcion tuple lo convertimos en tupla
    

    
    archivos_listado=[]#almacen elemento que hay en la ruta
    
    #recorre los elemento de la ruta
    for f in os.listdir(carpeta):
        if f.endswith(extesiones):
            archivos_listado.append(f)
            
    #renombre los archivos

    for i, nombre_actual in enumerate(archivos_listado,start=1):
        nuevo_nombre=f'{prefijo}{i:03}{extesiones}'
        print(nuevo_nombre)
        ruta_actual=os.path.join(carpeta,nombre_actual)
        print (f'ruta actual {ruta_actual}')
        ruta_nueva=os.path.join(carpeta,nuevo_nombre)
        print(f'nueva ruta {ruta_nueva}')
        os.rename(ruta_actual,ruta_nueva)
        
    messagebox.showinfo('éxito',f'renombrado completo')
    

#-------------INTERFAZ GRAFICA----------------------
ventana=tk.Tk()
ventana.title('renombrar archivos')
ventana.geometry('400x200')
ventana.resizable(False,False)

tk.Label(ventana,text='Carpeta de trabajo').pack(pady=5)
frame_carpeta=tk.Frame(ventana)
frame_carpeta.pack()    
entrada_carpeta=tk.Entry(frame_carpeta,width=40)
entrada_carpeta.pack(side=tk.LEFT,padx=5)
tk.Button(frame_carpeta, text="examinar", command=seleccionar_carpeta).pack(side=tk.LEFT)

tk.Label(ventana,text='Prefijo de los archivos').pack(pady=5)
entra_prefijo=tk.Entry(ventana,width=30)
entra_prefijo.insert(0,"imagen_")# apartir del caracter 0 insertar el prefijo
entra_prefijo.pack()

tk.Label(ventana,text='Extesiones de los archivos (separadas por comas):').pack(pady=5)
entra_extesiones=tk.Entry(ventana,width=30)
entra_extesiones.insert(0,".jpg,.png")# apartir del caracter 0 insertar el prefijo
entra_extesiones.pack()

tk.Button(ventana,text='Renombrar archivos', command=renombrar_archivos,bg='#04ba04',fg='white').pack(pady=10)

ventana.mainloop()








    




