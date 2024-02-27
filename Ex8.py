continua = 's'
while continua == 's':
    print("Digite a altura da caixa: ")
    altura = float(input())
    print("Digite o comprimento da caixa: ")
    comprimento = float(input())
    print("Digite a largura da caixa: ")
    largura = float(input())

    volume = altura * comprimento * largura
    print("Volume da caixa =  ", volume)

    print("Deseja continuar outra operacao? (S ou N)")
    continua = input()
