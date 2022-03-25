ele="Aluminio","Al","Azufre","S","Bismuto","Bi","Cloro","Cl","Mercurio","Hg"

def encuentraNom():
    nom=input("Escribe el nombre del elemento quimico: ")
    if nom.capitalize() in ele:
        nom=ele.index(nom.capitalize())
    print ("El simbolo del elementos es: ",ele[int(nom)+1])

def encuentraSim():
    sim=input("Escribe el simbolo del elemento quimico: ")
    if sim.capitalize() in ele:
        sim=ele.index(sim.capitalize())
    print ("El nombre del elementos es: ",ele[int(sim)-1])

opcion=-1
while opcion !=0:
    print("\nMenu de opciones:")
    print("1 - Buscar por elemento")
    print("2 - Buscar por simbolo")
    print("0 - salir")
    opcion = eval(input("Escriba opcion: "))
    if opcion ==1:
        encuentraNom()
    if opcion==2:
        encuentraSim()
   