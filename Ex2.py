cont = 1
nota = 0
soma = 0

while cont <= 5:
    print("Digite a nota: ", cont)
    nota = float(input())
    soma +=nota
    cont+=1


print("Soma das notas = ", soma)
media = soma/5
print("Media das notas = ", media)