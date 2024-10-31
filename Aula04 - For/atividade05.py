#Atividade 05




listaNumeros= []
index=0
numerosPositivos = 0
numerosNegativos = 0

print ("Digite 10 numeros inteiros")
for i in range(1,11):
    listaNumeros.append(int(input(f"Digite o numero {i}: ")))
    if listaNumeros[index] >= 0 :
        numerosPositivos += 1
    else:
        numerosNegativos += 1
    index += 1
print (f"Sao {numerosNegativos} numeros negativos")
print (f"Sao {numerosPositivos} numeros positivos")