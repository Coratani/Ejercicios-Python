numeros=list(range(1,101))
contador=0
suma=0
resto=0
for numero in numeros:
    while contador<numero:
        resto=numero%2
        contador=contador+1
    if numero in range(20,31):
        continue
    elif resto==0:
        suma=suma+numero
       
print("la suma es",suma)    
    