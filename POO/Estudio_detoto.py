""" def numero(num):
    if num % 2==0:
        return True
    

nu= [1,2,3,45,67,98,345]
print(list(filter(numero,nu))) """

""" nu= [1,2,3,45,67,98,345]
print(list(filter(lambda numero_par: numero_par % 2==0,nu))) """

#La funcion filtre se utiliza para filtrar objetos

""" class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo = cargo
        self.salario= salario
        
    def __str__(self):
        return('el empleado {} tiene un cargo de {} con un saladio {}'.format(self.nombre,self.cargo,self.salario) )
        

Listaempleado=[
    Empleado('Juan','administrador',11000000),
    Empleado('Ana Maria','abogado',7000000),
    Empleado('Argelio ramos','abogado',11000000)
]

salario_alto = filter(lambda e:e.salario >0,Listaempleado)

for a in salario_alto:
    print (a) """
    

# def elevar(numero):
#     return pow(numero,2)
# numero = list(range(1,11))
# print(numero)
# elevado= list(map(elevar,numero))
# print(elevado)

""" Crear un aplicativo que genere inicialmente un listado de estudiantes con 4 notas diferentes del semestre, 
cada una equivale al 25%. Haga que el listado de estudiantes pase por una función que les calcule el promedio. 
Finalmente filtre el listado de estudiantes solo con los que ganaron el semestre. Las notas de los estudiantes
deben estar entre 0 y 5, y para ganar el promedio debe ser mayor o igual a 3. Es requisito que para este funcionamiento 
se utilice las funciones lambda, filter y map.
 """
 

class Estudiantes:
    def __init__(self,n1,n2,n3,n4):
         self.nota1=n1
         self.nota2= n2
         self.nota3= n3
         self.nota4= n4
                 
    def promedio(self):
             self.promedio= (self.nota1+self.nota2+self.nota3+self.nota4)/4
             return self.promedio
         
    
         
    def __str__(self):
            return self.promedio
 
def Prome(n1, n2,n3, n4):
     return (n1 + n2+n3+ n4)/4
 
estudiantes =[ Estudiantes (1,2,3,4),
               Estudiantes (4,2,3,4),
              Estudiantes (3,5,5,2)
              ]  

def mayor(nota):
     return nota >=3 
     
promedio = list(map(lambda e:e.promedio(),estudiantes))

notaMayor= list(filter(mayor,promedio))
print(notaMayor)

do while












