contador=int(0)


def adivinanza():
    respuesta=input('De que color es el caballo blanco de santiago?')
    global contador
   
    if respuesta=='blanco':
        contador=int(contador+1)
        print('ganaste! Acertado en ',contador,'intento(s)')
        
    else:
        
        print('Fallaste! Intentalo de nuevo')
        contador=contador+int(1)
        adivinanza()
        
        
        
adivinanza()