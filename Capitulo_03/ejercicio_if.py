jugador1=input()
jugador2=input()

if jugador1==jugador2:
    print("empate")
elif jugador1=="piedra" and jugador2=="tijera":
    print("jugador 1 gana")
    
elif jugador1=="papel" and jugador2=="piedra":  
    print("jugador 1 gana")
elif jugador1=="tijera" and jugador2=="papel":  
    print("jugador 1 gana")
else:
    print("jugador 2 gana")
        