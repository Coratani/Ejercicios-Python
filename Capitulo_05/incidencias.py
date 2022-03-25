
print("gestion de incidencias".upper().center(80,"-"))
incidencia=input('Indique la incidencia: ')
cuentapaneles=incidencia.lower().count("panel")
if 'aviso' or 'error' in incidencia.lower():
    if 'conmutador' in incidencia.lower():
        if "conmutador verde" in incidencia.lower():
            print('Atasco en puerta de salida'.upper())
        elif "conmutador azul"in incidencia.lower():
            print('Reponer aceite en cinta'.upper())
        else:
            print('incidencia no reconocida')
    
    elif "panel" in incidencia.lower():
        if "panel" in incidencia.lower():
            print("detectado error en".upper(),cuentapaneles,"panel(es)".upper())
        else:
            print('incidencia no reconocida')
    else:
        print('incidencia no reconocida')