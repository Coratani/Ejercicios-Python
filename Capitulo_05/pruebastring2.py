print('resultado del clasico'.upper())
cadena=input('indique el resultado en formato Equipo1 Goles Equipo2 Goles: ')
espacios=cadena.count(' ') #solo admitiremos 3 espacios
if espacios !=3:
    print('el formato escrito es erroneo')
else:
    posBarc=cadena.lower().find('barcelona')
    posMadr=cadena.lower().find('madrid')
    if posBarc==-1 or posMadr==-1:
        print('los equipos no son correctos')
    else:
        if posBarc<posMadr:
            print('el partido se jugo en el camp nou')
        else:
            print('el partido se jugo en el santiago bernabeu')