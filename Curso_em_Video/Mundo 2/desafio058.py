# Melhore o desafio 28, onde o computador vai pensar em um numero entre 0 e 10 só que
#agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. 

import random 

n_usuario = int(input("Digite um número entre 0 e 10: "))
n_pc = random.randint(0,10)

while n_usuario != n_pc:
    n_usuario = int(input("Não foi dessa vez. Digite um número entre 0 e 10: "))

print("Parabéns, você acertou!")

    
