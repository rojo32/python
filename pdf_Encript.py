"""este script encripta un pdf, es necesario instalar pypdf2"""
from PyPDF2 import PdfReader,PdfWriter
import os


def encriptPDF(ruta):
    print('se evalua la ruta', ruta)
    
    if (os.path.isfile(ruta)):
        reader = PdfReader(ruta)
        writer=PdfWriter()
        for page in reader.pages:
             writer.add_page(page)
        writer.encrypt('12345')
        print('---------')
        
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),'PDF\encrip.pdf')# ruta actual
        print(ruta)
        with open(ruta,'wb')as f:
            writer.write(f)
        
        return True
            
    else:
        return False


print('\nEste script encripta un archivo  PDF asegurece de crear la carpeta PDF \n luego pegue el pdf en dicha ruta')
respuesta=input('desea continuar S/N ')

if (respuesta.lower()=='s'):

    ruta_script = os.path.dirname(os.path.abspath(__file__))# ruta actual
    carpeta = os.path.join(os.path.join(ruta_script,'PDF'),'a.pdf')

    if encriptPDF(carpeta):
        print('archivo encriptado exitosamente')
    else:
        print('no fue posible encriptar el archivo')
else:
    pass


    


            


        
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    



