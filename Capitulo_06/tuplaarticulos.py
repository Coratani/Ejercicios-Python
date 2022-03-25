articulos="Abrigo",85.35,"camisa",32.45,"zapatos",28.15

def imprime(listado):
    contador=0
    while contador<len(listado):
        print(listado[contador].ljust(10)+
              str(listado[contador +1]).rjust(5)+"$")
        contador+=2
"""     
def esprecio(elem):
    if isinstance(elem,str):
        return False
    else:
        return elem
def esarticulo(elem):
    valor=elem if isinstance(elem,str) else False
    return valor
"""
def descuentos(elem):
    if elem >= 50:
        elem-=(elem *0.3)
    elif elem>= 30:
        elem-=(elem*0.2)
    return elem

print("Los articulos comprados son:")
imprime(articulos)
#soloprecios=tuple(filter(esprecio,articulos))
#soloarticulos=tuple(filter(esarticulo,articulos))
soloprecios=tuple(filter(lambda e:False if isinstance(e,str) else e,articulos))
soloarticulos=tuple(filter(lambda e:e if isinstance(e,str)else False,articulos))
precioscondescuento=tuple(map(descuentos,soloprecios))

print('el total de los articulos es %4.2f$' %sum(soloprecios,2))
print('el total con descuento es %4.2f$'%sum(precioscondescuento,2))
articulos_final=tuple(zip(soloarticulos,precioscondescuento))
print("\nListado final de articulos:")
for artic in articulos_final:
    print("%3.2f$ ... %s" %(artic[1],artic[0]))
