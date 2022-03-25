import time
from time import sleep as pausa
print("Cuenta atras par acomenzar")
for cuenta in range(5,0,-1):
    print("{}...".format(cuenta))
    pausa(1)
epoca=time.time()
print("Segundos desde epoca:",epoca)
print("Escrito como fecha y hora local:",time.ctime(epoca))

estructura=time.localtime(epoca)
estructuraUTC=time.gmtime(epoca)
print("\nLa estructura local:",estructura)
print("La estructura en UTC:",estructuraUTC)
print("Con una estructura podemos obtener cualquier dato, por ejemplo año {} o dia {}"
      .format(estructura.tm_year,estructura.tm_mday))
print("Tambien de hora, son las {}:{}".format(estructura.tm_hour,estructura.tm_min))
print("\nEl montaje desde una estructura:",time.asctime(estructura))
print("El montaje personalizado:",
      time.strftime("dia %d del %m del año %Y a las %H horas",estructura))
print("Si a partir del montaje necesitamos el objeto struct_time:",
      time.strptime("dia 12 del 03 del año 2050","dia %d del %m del año %Y"))


