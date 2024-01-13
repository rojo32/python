"""este script busca directorio en  una direccion ip, adicional tiene la opcion de barra de progreso
https://www.youtube.com/watch?v=6umcGz4GTyY
"""

import argparse # pasar parametros 
import requests
from tqdm import tqdm


parser = argparse.ArgumentParser(description="Script de fuzzing de directorio Web")
parser.add_argument("url",help="ingrese url base")
parser.add_argument("diccionario", help="archivo diccionario")
args=parser.parse_args()

# abrimos el diccionario que fue pasado por argumento por parser
with open(args.diccionario) as file:
    wordlist= file.read().splitlines()# leer linea a linea cada elemento del archivo o diccionario

try:
    barra = tqdm(total=len(wordlist),desc="progreso", unit="urls", dynamic_ncols=True) # la dimencion de la barra es igual al total del diccionario
    for linea in wordlist:
        url_completa = args.url + linea
        response = requests.get(url_completa)

        if requests.status_codes==200:
            tqdm.write(f"directorio encontrado {url_completa}")
        barra.update(1)

except KeyboardInterrupt:
    print("\n script interupido por el usuario al pultsa CTRL + C")
finally:
    barra.close()
