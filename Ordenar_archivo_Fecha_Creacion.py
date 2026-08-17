from datetime import datetime
import os
import json
import shutil

def crear_carpeta(ruta_archivo, directorio_base):
    timestamp=os.path.getmtime(ruta_archivo)
    fecha=datetime.fromtimestamp(timestamp)
    carpeta_destino = fecha.strftime("%Y-%m")
    os.makedirs(os.path.join(directorio_base, carpeta_destino), exist_ok=True)

    return carpeta_destino


def organizar_archivo(directorio):
    #organizar los archivos en la carpeta
    log=[]

    #obtener ruta absoluta

    if not os.path.exists(directorio):
            print('Error: El directorio expecifico no existe')
            exit(1)
    
    print(f'\nSe organizaran los archivos en: {os.path.abspath(directorio)}')

    confirmacion=input("¿Desea continuar? (S/N):")
    
    if  confirmacion.lower().strip()=='s':              

        directorio=os.path.abspath(directorio)
        print(f'el directorio ingresado es {directorio}')
        #recorrer archivos
        for archivo in os.listdir(directorio):
            ruta_archivo=os.path.join(directorio,archivo)
            if not os.path.isfile(ruta_archivo) or archivo.startswith('.'):
                continue
            else:
                carpeta_destino=crear_carpeta(ruta_archivo, directorio)
                ruta_destino = os.path.join(directorio, carpeta_destino, archivo)
                print(f' ruta archivo {ruta_archivo} y ruta de destino a crear la carpta {ruta_destino} ')
                shutil.move(ruta_archivo, ruta_destino)
                log.append(f"{archivo} -> {carpeta_destino}/")  

        guardar_log(directorio, log)
        print(f"\nOrganización completada. {len(log)} archivos movidos." )   
    else:                     
        print('Operación cancelada')
        



def guardar_log(ruta,acciones):
    registro={
        "fecha_ejecucion": datetime.now().isoformat(),
        "directorio": ruta,
        "movimiento":acciones
    }
    with open("organizar_log.json","w",encoding="utf-8") as f:
        json.dump(registro,f,indent=2,ensure_ascii=False)



if __name__=='__main__':
    directorio=input('Ingrese la ruta del directorio a organizar(Enter para directorio actual) ')

    if not directorio:
        directorio='.'
    organizar_archivo(directorio)

    