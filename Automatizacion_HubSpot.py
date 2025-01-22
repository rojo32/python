# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import requests
import os
from urllib.parse import urlparse, parse_qs
from datetime import datetime


def download_onedrive_file(sharing_link, output_folder="Descargas"):
    """
    Descarga un archivo de OneDrive usando el enlace de compartir
    
    Args:
        sharing_link (str): El enlace de compartir de OneDrive
        output_folder (str): Carpeta donde se guardará el archivo descargado
    
    Returns:
        str: Ruta del archivo descargado
    """
    try:
        # Convertir el enlace de compartir al enlace directo de descarga
        if "1drv.ms" in sharing_link:
            response = requests.get(sharing_link, allow_redirects=True)
            sharing_link = response.url
            
        if "sharepoint.com" in sharing_link:
            download_link = sharing_link.replace("?web=1", "?download=1")
        else:
            #download_link = sharing_link.replace("view.aspx", "download.aspx")
            parsed_url = urlparse(sharing_link)
            params = parse_qs(parsed_url.query)
            
            # Construir el enlace de descarga directa
            base_url = f"https://{parsed_url.netloc}"
            if "resid" in params:
                download_link = f"{base_url}/download.aspx?share={params['share'][0]}"
            else:
                download_link = sharing_link.replace("view.aspx", "download.aspx")
                
         # Configurar headers para simular un navegador
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
            
            
            
            
         # Obtener la ruta de la carpeta de Descargas del usuario  
        downloads_folder = os.path.join(os.path.expanduser("~"), output_folder)
        # Ruta de la carpeta de destino (dentro de Descargas)
        output_folder = os.path.join(downloads_folder, "Colaborador")      
        

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Obtener el nombre del archivo del enlace
        file_name = os.path.basename(urlparse(sharing_link).path)
        if not file_name.endswith('.xlsx'):
            file_name = f"excel_file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            
        # Ruta completa del archivo
        file_path = os.path.join(output_folder, file_name)
        
             
        # Realizar la descarga con verificación de tamaño
        with requests.get(download_link, headers=headers, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            print(f"el tamaño es {total_size}")
            
            with open(file_path, 'wb') as file:
                downloaded_size = 0
                chunk_size = 8192
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)
                        downloaded_size += len(chunk)
                        
                # Verificar el tamaño descargado
                if total_size > 0 and downloaded_size != total_size:
                    raise Exception(f"Descarga incompleta: {downloaded_size} de {total_size} bytes")

        print(f"Archivo descargado: {file_path}")
        print(f"Tamaño: {downloaded_size / 1024:.2f} KB")
        return file_path

    except Exception as e:
        print(f"Error: {str(e)}")
        return None
# Ejemplo de uso
if __name__ == "__main__":
    # Reemplaza esto con tu enlace de OneDrive
    onedrive_link = "https://cidet-my.sharepoint.com/:x:/g/personal/argelio_ramos_cidet_org_co/EaawtcdgwWVGnNzA5objSAkBwlWvwyKyGewENn_c01K0XQ?e=roOxu0"
    downloaded_file = download_onedrive_file(onedrive_link)