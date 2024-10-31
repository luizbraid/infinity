# Atividade01

numero = int(input("Digite um numero inteiro: "))

soma = 0
sub = 0
mult = 0
div = 1.0

print ("Tabuada Soma")
for som in range(1,11):
    soma = numero + som
    print(f"{numero} + {som} =  {soma}")

print ("Tabuada Subtracao")
for sube in range(1,11):
    sub = numero - sube
    print(f"{numero} - {sube} =  {sub}")
print ("Tabuada multiplicacao")

for mul in range(1,11):
    mult = numero * mul
    print(f"{numero} * {mul} =  {mult}")
print ("Tabuada Divisao")

for divi in range(1,11):
    div = numero / divi
    print(f"{numero} / {divi} =  {div}")


