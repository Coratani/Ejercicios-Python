conjunto="italia","grecia","italia","china","grecia","brasil"
paises=set(conjunto)
europa=set({"francia","italia","españa","grecia","alemania","portugal"})

def listado(conjunto):
    for pais in conjunto:
        print(pais.ljust(15),end="")

paises.remove("china")
paises.add("turquia")
paises.add("alemania")

print("contenido actual del conjunto de paises:")
listado(paises)

print("\n\nContenido actual del conjunto de europa:")
listado(europa)
print("\n\ncontenido de los dos conjuntos:")
listado(paises | europa)
print("\n\nInteseccion de los dos conjuntos(elemntos en comun):")
listado(paises.intersection(europa))
print("\n\ndiferencia simetrica de lso dos conjuntos (elementos que"+
      " no estan a la vez en ambos conjuntos):")
listado(paises.symmetric_difference(europa))

paises.update(europa)
print("\n\nActualizacion de paises con el contenido de europa:")
listado(paises)