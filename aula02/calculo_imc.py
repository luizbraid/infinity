# Calculo de IMC

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = round(peso/(altura**2))

if imc < 18.5:
    print (f"Seu IMC é {imc} e classificado como Magreza")
elif imc >= 18.5:
    print (f"Seu IMC é {imc} e classificado como Normal")
elif imc >= 25:
    print (f"Seu IMC é {imc} e classificado como Sobrepeso")
elif imc >= 30 and imc < 40:
    print (f"Seu IMC é {imc} e classificado como Obesidade")
else:
    print (f"Seu IMC é {imc} e classificado como Obesidade Grave")