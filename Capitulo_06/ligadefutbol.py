print("\nLIGA DE FUTBOL")
equipos={"Fc Barcelona":0,
              "Atletico de Madrid":0,
              "Sevilla":0,
              "Celta":0,
              "Espanyol":0}
equip="Fc Barcelona","Atletico de madrid","Sevilla","Celta","Espanyol"
contador=0

for equipo in equipos:
    equipos.update({equipo:input("\nGoles del %s:"  %equip[contador])})
    contador=contador+1

def promedio():
    total=0
    i=len(equipos)
    for x in equipos.values():
        total=total+int(x)
        
    return total/i
def discr():
    quita1= equipos.pop(alt_max)
    quita2= equipos.pop(alt_min)
    return str(equipos)
alt_max=max(equipos,key=equipos.get)
alt_min=min(equipos,key=equipos.get)
gol1=equipos.get(alt_max)
gol2=equipos.get(alt_min)
print("\nPromedio de goles : ",promedio())
print("\nEquipo con maximo de goles({}): {}".format(gol1,alt_max))
print("\nEquipo con minimo de goles({}): {}".format(gol2,alt_min))
print("\nLa liga discriminando al maximo y al minimo queda: \n",discr())