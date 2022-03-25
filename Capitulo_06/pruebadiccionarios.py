def agregar():
    clave=input("escriba el nombre: ")
    valor=input("escriba la edad: ")
    dicc.setdefault(clave,valor)
def eliminar():
    clave=input("escriba el nombre a eliminar: ")
    print("eliminando %s ... %s"%(clave,dicc.pop(clave,"No encontrado")))
def listar():
    print("contenido del diccionario:")
    print(dicc)
    print("nombres".ljust(15)+"edades".rjust(5))
    for clave in dicc.items():
        print(clave[0].ljust(15)+clave[1].rjust(5))
        
dicc=dict()
opcion=-1
while opcion !=0:
    print("\nMenu de opciones:")
    print("1- agregar elementos")
    print("2-eliminar elementos")
    print("3-listar contenido")
    print("0 - salir")
    opcion = eval(input("Escriba opcion: "))
    if opcion ==1:
        agregar()
    if opcion==2:
        eliminar()
    if opcion==3:
        listar()
print("Gracias por usar el programa")        
    