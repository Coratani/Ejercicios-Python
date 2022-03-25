nombre='Sra Alfredo Villar'
print('nombre original',nombre)
nombre=nombre.replace('Sra','sr')
print('genero cambiado:',nombre)
nombre=nombre.lstrip('sr ')
print('sin formalismos',nombre)

print('\nCambio de texto dinamico:')
cadena='bienvenido a mi programa {0}'
print('original:',cadena)
print('Formateado:',cadena.format('en Python'))

cadena='importe bruto: {0}$+ IVA: {1}$=Importe neto {2}$'
print('\noriginal:',cadena)
print('formateado:',cadena.format(100,21,121))

cadena='importe bruto: {bruto}$ + IVA: {iva}$= Importe neto: {neto}$'
print('\noriginal:',cadena)
print('Formateado:',cadena.format(iva=21,neto=121, bruto=100))