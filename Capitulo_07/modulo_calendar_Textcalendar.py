import calendar

año=eval(input("Escribe el año: "))
mes=eval(input("Escribe el mes: "))

calendario=calendar.TextCalendar()
print("El calendario del mes:\n",calendario.formatmonth(año,mes,5,3))
print("El calendario anual, en 2 filas: ")
calendario.pryear(año,m=6)