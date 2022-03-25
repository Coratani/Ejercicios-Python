miweb = input("De que es tu pagina web?   ")
if miweb=="noticias":
    print("Mi web es sobre noticias")
    
elif miweb=="deportes":
    print("Mi web es sobre deportes")
elif miweb=="cine":
    print("Mi web es sobre el mundo del cine")
else:
    print("Mi web es sobre otra cosa")
edad=int(input("que edad tienes?:  "))
mensaje="Eres mayor de edad" if edad>=18 else"Eres menor"
print(mensaje)
    
print("fin del programa")

