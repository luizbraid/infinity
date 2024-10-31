# # FOR com Condicionais

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f"{i} é par")



texto = input("Digite uma frase: ")
contador_vogais = 0

for caracter in texto:
    if caracter.lower() in "aeiou":
        contador_vogais += 1
        
print (f"A frase possui {contador_vogais} vogais")


