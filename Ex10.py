soma = 0
media = 0

for cont in range(1, 6):
    print("Digite a nota: ", cont)
    nota = float(input())
    soma+= nota

media = soma / 5
print("Media das notas = ", media)