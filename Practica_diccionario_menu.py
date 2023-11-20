# programa que solicita informacion sobre de unos usuario, y las almacena en un diccionario, para luego
# consultar, eliminar, listar.

def agregar():
    global usuario
    
    id=input('ingresa la identificaciòn ')
    nombre=input('ingresa la nombre ')
    apellido=input('ingresa la apellido ')
    tel=input('ingresa la telefono ')
    
    usuario[id]=id,nombre, apellido,tel
    print (usuario)
    
def eliminar(id):
    
    if id in usuario:
        del usuario[id]
        print('EL elemento fue eliminado')
    else:
        print('el id no existe')
 
def consultar(id):
    if id in usuario:
        r=usuario.get(id)  
        print(r)

def listar():
    for u in usuario:
        print(
            """id: {}
            nombre: {}
            apellido: {}
             direccion: {}
             telefono: {}""".format(usuario[u][0], usuario[u][1],usuario[u][2],usuario[u][3],usuario[u][4])
            
            
        )
usuario= {}
def menu():
    
    while True:
    
        print(" **** Selecciones la opcion del menù **** \n")
        print("[1] **** agregar elementos ****")
        print("[2] *** Eliminar elementos ****")
        print("[3] *** consultar elementos ****")
        print("[4] *** listar elementos ****")
        print("[5] *** salir ****")
        
        
        opcion = int(input("Ingrese la opciòn: "))
        if opcion ==1:
                agregar()
        elif opcion ==2:
                op=input('Ingrese el id: ')
                eliminar(op)
        elif opcion ==3:
                op=input('Ingrese el id a consultar: ')
                consultar(op)
        elif opcion ==4:
            listar()                           
                
        elif opcion ==5:
                exit()
       
            
menu()   
    

    