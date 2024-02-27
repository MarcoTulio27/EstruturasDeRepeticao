cont = 1
numNeg = 0

while cont <=5:
    print("Digite o numero: ")
    num1 = float(input())
    if num1 < 0:
        numNeg += 1
    cont += 1


print("Valores negativos: ", numNeg)