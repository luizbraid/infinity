print ("Calculo de IMC")
altura = float(input("Favor digite a altura: "))
peso = float(input("Digite o valor da peso: "))

IMC = round(peso /(altura * altura), 2)

print ("O IMC é  ", IMC)