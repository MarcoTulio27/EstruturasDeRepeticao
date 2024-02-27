numNeg = 0
for cont in range(1, 6):
    print("Digite um valor: ")
    num1 = float(input())
    if num1 < 0:
        numNeg += 1

print("Quantidade de valores negativos: ", numNeg)