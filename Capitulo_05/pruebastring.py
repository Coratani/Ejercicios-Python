cadena='esta cadena de texto me sirve de prueba'
print(cadena.capitalize()+'-primera letra mayuscula-')
print(cadena.upper()+'-cadena pasada a mayuscula')
print(cadena.title()+'=primera letra de cada palabra en mayusculas')
print(cadena.title().swapcase()+
      ' = a partir del resultado anterior intecambiamos mayus/minus-')
print(cadena.ljust(60,'=')+'-la cadena ocupa un total de 60 caracteres-')
print(cadena.rjust(60)+
      '-igual pero alineado a la derecha y usando espacios por defecto-')
cantidad='859.34'
print(cantidad.zfill(10)+
      ' -llena con ceros a la izquierda hasta completar 10 caracteres de longitud-')