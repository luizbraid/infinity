# Atividade 06

listaPares = []
total = 0
index = 0

for i in range(1, 51):
    if i % 2 == 0:
        listaPares.append(i)
    for n in listaPares:
        total += n
print (total)




