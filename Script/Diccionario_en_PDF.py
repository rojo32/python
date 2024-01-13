""" este script permite quitar la contraseña de un PDF, por medio de diccionario"""
import  PyPDF2
import os

def descript(diccionario, pdf):
    print(diccionario)
    print(pdf)
    bandera = False
     
    pdf_pass = PyPDF2.PdfReader(pdf)
    
    try:
     
        with open(diccionario,encoding='utf8') as f:
            for linea in f:
                print(f' --> {linea}')
                pasword = linea.strip()#eliminamos los espacios en caso de que existan
                if pdf_pass.decrypt(pasword)!=0:
                    print(f'La contraseña es {pasword} :)')
                    bandera = True
                    break
            
            
                
    except Exception as e:
        print(f'ha ocurrido un error de tipo {e}')    
    
    if bandera == False:
        print(':( no se encontro la contraseña')
        
    
            

ruta_pdf= os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'PDF'),'encrip.pdf')
ruta_diccionario=os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'PDF'),'Diccionario.txt')

descript(ruta_diccionario,ruta_pdf)
   
    

            
     