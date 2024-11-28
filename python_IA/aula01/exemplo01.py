# Adicionando itens ao final da lista com o metodo .append()
numeros = [1,2,3,4,5]

numeros.append(6)

print (numeros) #[1,2,3,4,5,6]

#Adicionando itens em dada posição da lista com metodo .insert()
numeros = [10,30,40,50]
letras = ['a','e','o','u']
pesos = [1.2,3.4,5.3,6.7]

#Inserindo valores nas respectivas posições das listas
numeros.insert(1,20) #Inserindo 20 na posição 1
letras.insert(2,'i') #Inserindo 'i' na posição 2
pesos.insert(2,4.0) # Inserindo 4.0 na posição 2 

# Exibindo as inserções de valores
print (numeros) #[10,20,30,40,50]
print (letras) # ['a','e','i','o','u']
print (pesos) # [1.2,3.4,4.0,5.3,6.7]