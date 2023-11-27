""" herencia"""

class Vehiculo:
    def __init__(self,color, rueda):
        self.color=color
        self.rueda=rueda

    def __str__(self):
        return 'color: {} rueda: {}'.format(self.color,self.rueda)


class Coche(Vehiculo):
    def __init__(self, color, rueda,velocidad):
        super().__init__(color, rueda) 
        self.velocidad=velocidad

    def __str__(self):
        return super().__str__() + ' velocidad (km/h):'+str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, rueda,tipo):
        super().__init__(color, rueda)
        self.tipo=tipo

    def __str__(self):
        return super().__str__()+ ' tipo: '+self.tipo
    

#creamos los objeto tipo vehiculos

Vehiculo = Vehiculo('azul',4)
print(Vehiculo)

# creamos el objecto coche
Toyota= Coche('rojo',4,200)
print(Toyota)

#bicicleta
bici = Bicicleta('blanco',2,'urbano')
print(bici)
    
        