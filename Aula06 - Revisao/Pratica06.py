print("Calculo de Desconto")

valor_produto = float (input("Digite o valor do produto: "))
valor_desconto = float (input("Digite o valor do desconto/percente: "))
valor_desconto /= 100

valor_final = valor_produto - (valor_produto * valor_desconto)

print (valor_final)



