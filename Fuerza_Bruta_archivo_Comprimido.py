""" este script permite realizar fuerza bruta a un archivo comprimido 
para obtener su clave de acceso """
import itertools
import zipfile
import os

#name = "archivo.zip"
opciones = '123456'
name = input('Ingrese el nombre del archivo comprimido, este debe estar en la misma ruta py ')
ruta_script = os.path.abspath(__file__)
ruta_archivo = os.path.join(os.path.dirname(ruta_script), name)
print(ruta_archivo)


if os.path.exists(ruta_archivo):
    for x in itertools.product(opciones, repeat=6):
        opciones = ''.join(opciones)
        print(f'{x} {opciones}')
    try:
        with zipfile.ZipFile(ruta_archivo, 'r') as zip_ref:
            zip_ref.extractall(pwd=opciones.encode('utf-8'))
            print('archivo extraido exitosamente')
    except Exception as e:
        print(f'Ups! ocurrio un error {e}')
else:
    print('el archivo no exite en la ruta')
            
            
