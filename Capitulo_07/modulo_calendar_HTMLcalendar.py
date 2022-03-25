import calendar

año=eval(input("Escribe el año: "))
mes=eval(input("Escribe el mes: "))

calendario=calendar.LocaleHTMLCalendar(locale='')
calendario.cssclasses=["mon","tue","wed","thu","fri","sat","sun"]
calendario.cssclass_noday="enblanco"
calendario.cssclass_month="mes"
calendario.cssclass_year="anyo"
calendario.cssclass_year_head="anyo_h"
cal=calendario.formatyearpage(año,4,'calendario_estilos.css')

nombre='calendario_%s.html'%año
file=open(nombre,'wb')
file.write(cal)
file.close()
print("Archivo '%s' creado en la misma ubicacion que este programa"%nombre)
