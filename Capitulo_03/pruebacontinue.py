nombres=['alejandro','merche','adela','carmelo']
for nombre in nombres:
    if nombre=='merche':
        nombre= 'mercedes'
    print(nombre)
print('fin de la lista')

numeros=range(10,0,-1)
print('esta es la tabl de multiplicar del 5:')
for numero in numeros:
    if numero==5:
        continue
    print('5 x',numero,'=',5 *numero)
print('eso es todo')