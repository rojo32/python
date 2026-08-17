#!/usr/bin/env python3
"""
unir_pdfs.py

Une todos los PDF de una carpeta en un solo archivo, en orden numerico
(1_, 2_, 3_ ... 10_), manejando automaticamente archivos cifrados/protegidos.

Uso:
    python3 unir_pdfs.py                     -> usa la carpeta actual
    python3 unir_pdfs.py /ruta/a/la/carpeta   -> usa la carpeta indicada
    python3 unir_pdfs.py /ruta -o salida.pdf  -> nombre de salida personalizado

Requiere:
    pip install pypdf --break-system-packages
"""

import sys
import re
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def clave_orden_natural(nombre: str):
    """Ordena '2_archivo.pdf' antes que '10_archivo.pdf' (orden natural, no alfabetico)."""
    partes = re.split(r"(\d+)", nombre)
    return [int(p) if p.isdigit() else p.lower() for p in partes]


def cargar_pdf(ruta: Path) -> PdfReader:
    """Carga un PDF, desencriptandolo automaticamente si es necesario."""
    lector = PdfReader(str(ruta))
    if lector.is_encrypted:
        # La mayoria de PDFs 'cifrados' por exportadores no tienen contrasena real,
        # solo restricciones de edicion. Una contrasena vacia suele bastar.
        try:
            lector.decrypt("")
        except Exception:
            pass
    return lector


def unir_pdfs(carpeta: Path, salida: Path):
    print(f"Buscando PDFs en: {carpeta}")

    # Busca .pdf y .PDF (y variantes de mayusculas/minusculas)
    encontrados = {}
    for p in carpeta.iterdir():
        if p.is_file() and p.suffix.lower() == ".pdf":
            encontrados[p.resolve()] = p

    archivos = sorted(encontrados.values(), key=lambda p: clave_orden_natural(p.name))
    archivos = [a for a in archivos if a.resolve() != salida.resolve()]

    if not archivos:
        print(f"No se encontraron archivos .pdf en: {carpeta}")
        print("Archivos que SI se encontraron en esa carpeta:")
        for p in carpeta.iterdir():
            print(f"  - {p.name}")
        sys.exit(1)

    print("Orden en que se uniran los archivos:")
    for i, a in enumerate(archivos, 1):
        print(f"  {i}. {a.name}")

    escritor = PdfWriter()
    con_problemas = []

    for archivo in archivos:
        try:
            lector = cargar_pdf(archivo)
            for pagina in lector.pages:
                escritor.add_page(pagina)
        except Exception as e:
            con_problemas.append((archivo.name, str(e)))
            print(f"  [AVISO] No se pudo procesar '{archivo.name}': {e}")

    with open(salida, "wb") as f:
        escritor.write(f)

    print(f"\nListo. Archivo generado: {salida}")
    if con_problemas:
        print("\nArchivos que tuvieron problemas y NO se incluyeron:")
        for nombre, err in con_problemas:
            print(f"  - {nombre}: {err}")


def main():
    parser = argparse.ArgumentParser(description="Une todos los PDF de una carpeta en uno solo.")
    parser.add_argument("carpeta", nargs="?", default=".", help="Carpeta con los PDF (por defecto: carpeta actual)")
    parser.add_argument("-o", "--salida", default="resultado_final.pdf", help="Nombre del archivo de salida")
    args = parser.parse_args()

    carpeta = Path(args.carpeta).expanduser().resolve()
    salida = carpeta / args.salida

    unir_pdfs(carpeta, salida)


if __name__ == "__main__":
    main()