# def mensaje():
#     print("hola, que tal?")
#     
# def sumador():
#         num1=10
#         num2=15
#         return num1+num2
# 
# mensaje()
# suma=sumador()
# print(suma
#

# def nombrecompleto(nombre, apellidos="-Sin apellidos-"):
#     return"te llamas "+apellidos+", "+nombre
# 
# print(nombrecompleto("irene","rosales"))
# print(nombrecompleto("Juan carlos"))
# print(nombrecompleto(apellidos="ruiz sancho", nombre="isabel"))
def usuario(nombre,*aficiones,**datos):
    print("te llamas "+ nombre+" y tus aficiones son:")
    texto=""
    for aficion in aficiones:
        texto=texto+aficion+","
    print(texto)
    for dato in datos:
        if dato == "padre":
            print("tu padre se llama "+datos[dato])
        if dato=="madre":
            print("Tu madre se llama "+datos[dato])
usuario("Jose","nadar","pasear","pescar","bailar",padre='mateo',madre='luisa')

listadatos=['gregorio','pasear','montar en bici','dormir']
listadatospersonales={'madre':'julia','padre':'Manuel'}
usuario(*listadatos,**listadatospersonales)
