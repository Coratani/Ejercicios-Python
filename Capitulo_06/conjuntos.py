Calabria=set({'Cantazaro','Cosenza','Crotona','Reggio de calabria','Vibo Valentia'})
Campania=set({'avellino','Benevento','Caserta','Napoli','Salerno'})
Lacio=set({'Frosinone','Latina','Rieti','Roma','Viterbo'})
Ligeria=set({'Genova','Imperia','La Spezia','Savona'})
Lucrania=set({'Matera','Potenza'})
Molise=set({'Campobasso','Isernia'})
Toscana=set({'Arezzo','Florencia','Grosseto','Livorno','Lucca','Massa-Carrara','Pisa','Pisotia','Prato','Siena'})
Umbria=set({'Perusa','Terni'})
Veneto=set({'Belluno','Padua','Rovigo','Treviso','Venecia','Verona','Vicenza'})
Ita=Calabria,Campania,Lacio,Ligeria,Lucrania,Molise,Toscana,Umbria,Veneto
tuplaIta="Calabria","Campania","Lacio","Ligeria","Lucrania","Molise","Toscana","Umbria","Veneto"
prov=input("Introduzca la provincia italiana: ")
prov=prov.capitalize()
i=0
region=""
# regprnt=tuplaIta[i]
def encuentra(region):
    if prov in region:
        return True
    else:
        return False
# def     
    
while i<len(Ita):
    if encuentra(Ita[i]):
        region=Ita[i]
        regprnt=tuplaIta[i]
    i=i+1    
if region=="":
    print("La provincia no ha sido encontrada")
else:
    todas=set()
    todas.update(Calabria,Campania,Lacio,Ligeria,Lucrania,Molise,Toscana,Umbria,Veneto)
    print("\nLa región de %s es %s" % (prov, regprnt))
    region.remove(prov)
    print("\nSus provincias son: ")
    for nom in region:
        print(nom.ljust(10),end="")
    print("\n\nLas provincias de Italia en conjunto son:")   
    for nombre in todas:
        print(nombre.ljust(10),end=" ")
