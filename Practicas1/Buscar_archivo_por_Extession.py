"""script que busca un archivo en una ruta por extesion"""
import os

def buscar_archivos(ruta,extension):
    # Lista para almacenar rutas de archivos .mp3
    rutas = []
    
    # Recorre todos los directorios y archivos dentro de la ruta
    for root, _, archivos in os.walk(ruta):
        for archivo in archivos:
            # Verifica si el archivo tiene la extensión .mp3 (ignora mayúsculas/minúsculas)
            if os.path.splitext(archivo)[1].lower() == extension:
                rutas.append(os.path.join(root, archivo))  # Guarda la ruta completa del archivo
    
    return rutas

# Solicita al usuario la ruta del directorio
ruta = input('Ingrese la ruta del directorio a realizar la búsqueda: ')
extension = input('Ingrese la extesión que deseas ingresar (ejemplo .pdf): ')

# Busca los archivos .mp3 en la ruta proporcionada
archivos_mp3 = buscar_archivos(ruta,extension)

# Muestra los resultados
if archivos_mp3:
    print(f"Se encontraron los siguientes archivos con la extesión {extension}:")
    for archivo in archivos_mp3:
        print(f' -> {archivo}')
else:
    print("No se encontraron archivos .mp3 en la ruta proporcionada.")

            
            
        
        
    