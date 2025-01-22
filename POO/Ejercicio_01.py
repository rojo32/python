"""se crea 3 objeto tipo cliente, el cual es pasado como parametro a la clase empresa como lista"""

# se crea la clase cliente
class Clientes:
    def __init__(self, cedula, nombre, apellido, email, celular):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido= apellido
        self.email=email
        self.celular = celular

    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    

# creamos la clase empresa

class Empresa:
    def __init__(self,cliente=[]):
        self.cliente=cliente

    def MostrarCliente(self, cedula=None):
        for c in self.cliente:
            if c.cedula==cedula:                
                return c
        return 'cliente no existe'

    def BorrarCliente(self,cedula=None):
        print(cedula)
        for i,c in enumerate(self.cliente):            
            if c.cedula==cedula:
                del self.cliente[i]
                return 'elemento eliminado'        
        return 'El cliente no exite'
    
    def Listar(self):
        print('\nNombre | apellido | cedula')
        for i, c in enumerate(self.cliente):
            #print('el nombre: {} el apellido: {} la cedula es: {}'.format(self.cliente[i].nombre,self.cliente[i].c.apellido, self.cliente[i].c.cedula))
            print('{}     {}       {}'.format(c.nombre,c.apellido, c.cedula))

    def __del__():
        return 'has llamado elimiar objeto'


juan =Clientes(123,"juan","lora","j@fmail.com","3104082265")
diana =Clientes(456,"Diana","lora","d@fmail.com","3104085588")
oscar =Clientes(789,"oscar","lora","o@fmail.com","3104086677")

E = Empresa([juan,diana,oscar])
E.Listar()
E.__delattr__
#print(E.BorrarCliente(123))
#print(E.MostrarCliente(1233))



            




        
