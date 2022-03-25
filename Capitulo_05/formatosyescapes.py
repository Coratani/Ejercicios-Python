linea="\tpais\tmoneda\n"
pais=""
while "salir" not in pais:
    pais=input("nombre del pais(escribe\"salir\"para salir): ")
    if "salir" not in pais:
        moneda=input("moneda para \'"+pais+"\': ")
        linea+="\t" +pais+"\t"+moneda+"\n"
        print("\n\nRESULTADOS: \n %s" % linea)

cuentaEuros=linea.lower().count("euro")
cuentaLineas=linea.count("\n")-1
print("Hay %i veces \"Euro\",lo cual es un %.2f%% de paises."
      % (cuentaEuros, cuentaEuros/cuentaLineas*100))
                       
