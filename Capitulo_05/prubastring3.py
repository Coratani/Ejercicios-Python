cadena=input('escriba un texto')

if cadena.isalnum():
    print('consta de letras y/o numeros sin espacios')
if cadena.isalpha():
    print('consta de letras,sin numeros y sin espacios')
if cadena.isdigit():
    print('consta solo de numeros,sin espacios')