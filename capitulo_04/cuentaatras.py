def cuenta_atras(numero):
    if numero==0:
        print('final de la cuenta')
    else:
        print(numero)
        cuenta_atras(numero-1)

cuenta_atras(3)