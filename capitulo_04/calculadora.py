# def suma():
#     a=int(input('Introduzca un numero '))
#     b=int(input('Introduzca otro numero'))
#     print("La suma es: "+(a+b))
    
def accio():
    operacion=input('quieres sumar,restar o salir?')
    suma=lambda a,b:a+b
    resta=lambda a,b:a-b

    if operacion=='sumar':
        a=int(input('Introduzca un numero '))
        b=int(input('Introduzca otro numero '))
        print("el resultado de la suma es: ")
        print(suma(a,b))
        accio()
    elif operacion=='restar':
        a=int(input('Introduzca un numero '))
        b=int(input('Introduzca otro numero '))
        print("el resultado de la suma es: ")
        print(resta(a,b))
        accio()
    elif operacion=='salir':
       quit()
    else:
        accio()
accio()

