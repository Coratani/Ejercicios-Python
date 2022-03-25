from datetime import datetime
hoy=datetime.now()
print("Fecha y hora actual:", hoy)
print("La fecha:",hoy.date()," y la hora:",hoy.time())
desglose=hoy.timetuple()
print("Podemos obtener cualquier atributo desglosado: Hora",
      desglose.tm_hour,"mes",desglose.tm_mon,"dia del año",desglose.tm_yday)
enIso=hoy.isoformat("#","hours")
print("Formato ISO con separador # y solo la hora", enIso)
cumple=datetime.fromisoformat("1985-08-26T06:25")
print("Mi cumpleaños fue el dia", cumple.day," a las", cumple.hour,"y",cumple.minute)