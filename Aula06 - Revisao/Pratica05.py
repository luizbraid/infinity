print ("Calculo da media do aluno")


nota01 = float(input("Digiteo valor da primeira nota: "))
nota02 = float(input("Digiteo valor da segunda nota: "))
nota03 = float(input("Digiteo valor da terceira nota: "))
nota04 = float(input("Digiteo valor da quarta nota: "))

media = round((nota01 + nota02 + nota03 + nota04)/4, 2)
print(media)

if media >= 6:
    print ("Aluno Aprovado")
else:
    print ("Aluno Reprovado")

