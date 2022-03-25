jugadores=[]
equipos=[]
listado=[jugadores,equipos]
jugador=''
while jugador.upper()!="FIN":
    jugador=input('nombre del jugador(fin para terminar): ')
    if jugador.upper()!="FIN":
        equipo=input("Nombre de su equipo")
        jugadores.append(jugador)
        equipos.append(equipo)
print("\n\nDatos Introducidos")
print("\n\nConsultas")
equipo=""
while equipo.upper() !="FIN":
    equipo=input("\nNombre del equipo (FIN para terminar): ")
    if equipo.upper() !="FIN":
        if equipo in equipos: #si existe...
            print("JUGADORES: ",end="")
            for i in range(len(equipos)):
                if listado[1][i]==equipo:
                    print(listado[0][i].ljust(20),end="")
        else:
            print("\nEquipo no encontrado.")