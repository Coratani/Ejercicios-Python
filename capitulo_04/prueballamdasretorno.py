"""Programa para demostrar el funcionamiento de las llamadas de retorno.

Se crean tres funciones diferenciadas por un numero, y se llaman de forma
dinamica mediante la funcion globals().

"""

def nivel1():
    'es la primera funcion definida'
    return'estes es nivel 1'
def nivel2():
    "es la segunda"
    return'este es el nivel 2'
def nivel3():
    """Es la tercera"""
    return 'este es el nivel 3'
def iniciar():
    """es la funcion principal.

    Solicita al usuario un numero,que servira
    paraformar el nombre de funcion que serea llamada.
    Tambien se comprueba si dicha funcion no existe."""
    
    num= input('indique el nivel que necesita: ')
    if 'nivel'+num in globals():
        if callable(globals()['nivel'+num]):
            print(globals()["nivel"+num]())
    else:
        print('el nivel ' + num+' no existe')
        
iniciar()

print("Documentacion nivel1: "+nivel1.__doc__)
print("documentacion iniciar: "+iniciar.__doc__)
print("documentacion general: "+__doc__)