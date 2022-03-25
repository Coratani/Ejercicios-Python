import os
import sys
import random
print("Ejemplos modulo os")
print("Carpeta de trabajo actual: ",os.getcwd())
if(os.path.exists(os.getcwd()+"\\soluciones")):
    print("Dispone de una carpeta de ssoluciones")
else:
    print("La carpeta soluciones no se encuentra")
    
    
def plataforma(dato):
    if dato.startswith('linux'):
        return "linux"
    if dato.startswith('darwin'):
        return "Mac OS X"
    if dato.startswith('win32'):
        return"Windows"
    else:
        return"(no reconocido)"
    
print("\nEjemplos modulos sys")
print("la ruta y nombre del interprete python es", sys.executable)
print("la plataforma de trabajo es", plataforma(sys.platform))
print("La informacion sobre esta version de Python es {}.{}.{}"
      .format(sys.version_info.major, sys.version_info.minor,sys.version_info.micro))

print("\nEJEMPLOS MODULO RANDOM")
random.seed(50)
linea="Diversos numeros al azar entre 1 y 10:\n"
for contador in range(10):
    linea=linea+" "+str(random.randint(1,10))
print(linea)

print("Otro ejemplo de 5 numeros al azar entre 100 y 200: {}".format(random.sample(range(100,200),5)))
  
lista=["Barcelona","Girona","Lleida","Tarragona"]
print("Una provincia al azar: {}".format(random.choice(lista)))
print("Dos provincias al azar: {}".format(random.sample(lista,2)))
random.shuffle(lista)
print("Todas las provincias mezcladas: {}".format(lista))