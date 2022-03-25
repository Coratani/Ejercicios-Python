import locale

def imprime(cantidad):
    print("\nUna cantidad monetaria con simblo local:",
      locale.currency(cantidad,symbol=True,grouping=True))
    print("La misma cantidad con simbolo internacional:",
          locale.currency(cantidad,symbol=True,grouping=True,international=True))

locale.setlocale(locale.LC_ALL,'')
print("El codigo de lenguaje y codificacion local es", locale.getdefaultlocale())
imprime(45640.3645)

japon=locale.normalize("ja")
print("\nCodigo de configuracion regional de Japon normalizado:", japon)
japon=japon[:japon.find(".")]
print("Codigo de configuracion regional sin codificacion",japon)
locale.setlocale(locale.LC_ALL,japon)
imprime(45640.3645)