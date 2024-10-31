# Variavel de sequencia

# Lista de Strings, inteiro e Flutuantes

#Tuple < str | int | float >
#nomes = ("Joao","Pedro","Lucas",100,25.5)

#print (nomes)

#print (nomes[2])

#sobrenome = "Braid"
#nomes = ("Luiz","Eduardo","Nonato")

#Usando While
#index = 0
#while index <=2:
#    print(f"{nomes[index]} {sobrenome}")
#    index += 1

# Usando FOR
#for nome in nomes:
#    print(f"{nome} {sobrenome}" )


precosCarrinho = (10.50,29.90,51,89,100)

#while

total = 0
index = 0

while index < len(precosCarrinho):
    total += precosCarrinho[index]
    index += 1

print (total)


#FOR

total = 0
for preco in precosCarrinho:
    total += preco

print (total)



# Usando RANGE
#range(start)
#range(start, stop)
#range (start, stop, step)

for numero in range(5):
    print(numero)

for n in range(4,8):
    print(n)

for n in range(1,10,2):
    print(n)

palavra = "Python"
for letra in palavra:
    print(letra)
