numero=int(input('Introduzca un numero: ') or '10') 
total=int(1)    
def factorial(numero):
   
    global total
    if numero>=1000:
        quit()
    while numero>1:
        total*=numero
        numero-=1
    return total
if numero==10:
        print('El factorial del valor por defecto ',numero,'es ',factorial(numero))
else:
    print('El factorial de ',numero,'es ',factorial(numero))