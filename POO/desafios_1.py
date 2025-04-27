class Persona:
    def __init__(self,nombre,edad,genero,direccion): 
        self.nombre=nombre
        self.edad=edad
        self._genero=genero
        self._direccion=direccion

    #Metodo getter: leer los valores
    def get_genero(self):
        return self._genero
    
    def  get_direccion(self):
        return self._direccion
    

    #setter: Modificar los valores de un atributo
    
    def set_genero(self,genero):
         self._genero=genero

    def set_direccion(self,direccion):
         self._direccion=direccion

    def __str__(self): 
        return "{} {} {} {}".format(self.nombre,self.edad,self._genero,self._direccion)

    def consultar(self):
        return "el nombre del objecto es {} y su edad es {} genero {} y la direccion es {}".format(self.nombre, self.edad,self._genero,self._direccion)
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, direccion, numero_estudiante,lista_curso):
        super().__init__(nombre, edad, genero, direccion)
        self.numero_estudiante=numero_estudiante
        self.lista_cursos=lista_curso

    def imprimir(self):
        return super().consultar()+" el numero es: {} esta son las lista {}".format(self.numero_estudiante,self.lista_cursos)
    #






