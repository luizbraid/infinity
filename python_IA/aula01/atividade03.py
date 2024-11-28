#minha_lista=["zero",1,"dois",3.0,"quatro",5]
#print(minha_lista[3])



minha_lista = [
    23,
    17,
    84
]

resposta = input("Digite sua idade: ")
resposta_int = int(resposta)

print(f"Qual sua idade: {minha_lista}")
minha_lista.append(resposta_int)
print(f"Sua idade foi adicionada: {minha_lista}")