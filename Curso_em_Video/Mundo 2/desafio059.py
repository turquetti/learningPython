# crie um programa que leia dois valores e mostre um menu na tela
# 1. somar
# 2. multiplicar
# 3. maior
# 4. novos numeros
# 5. sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = 0

while operacao != 5:
    print('''
    1. Somar
    2. Multiplicar
    3. Maior
    4. Novos números
    5. Sair do programa
    ''')
    operacao = int(input("Digite a operação que deseja realizar: "))

    if operacao == 1:
        soma = n1 + n2
        print("Soma: ", soma)
    elif operacao == 2:
        multi = n1*n2
        print("Multiplicação: ", multi)
    elif operacao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior é: ", maior)
    elif operacao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif operacao == 5:
        print("Finalizando...")
    else: 
        print("Opção inválida")

print("Fim do programa, volte sempre!")

    


