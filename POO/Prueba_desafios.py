from  desafios_1 import Persona, Estudiante

lista= ['Ingles', 'Python', 'SQL', 'HTML', 'CSS']
Juan=Estudiante("juan", "18","masculino","Cl 92C #88-99","1",lista)
Juan.set_genero('Masculino')
print(Juan.get_genero())
print("---------------------------")
print(Juan.consultar())


