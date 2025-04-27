from math import pi,pow

def area(r):
    areaC= pi*2
    return areaC

valores=[1,3,0,-1,-3,2+3,True,'hola']

for v in valores:
    resultado=area(v)
    print(f'para el valor {v} el resutado es {resultado}')