print ("Categoria de Idade")

idade = int(input("Digite sua idade: "))

if idade <= 10:
    print("Criança")
elif idade > 10 and idade <= 15:
    print("Adolescente")
elif idade > 15 and idade <= 59:
    print ("Adulto")
else:
    print ("Idoso")

