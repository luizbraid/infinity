print("Calculo de juros")


capital_inicial = float(input ("Digite o valor do capital inicial: "))
valor_juros= float(input("Digite o valor do juros/mes: "))
tempo_investimento = float(input("Digite o tempo do investimento: "))



juros_simples = capital_inicial * valor_juros * tempo_investimento

print ("O valor do juros simples é: ", juros_simples)

