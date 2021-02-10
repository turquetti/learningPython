#Crie um programa que faça o computador jogar jokenpo com vc

import random 
jokenpo = ['pedra', 'papel', 'tesoura']

jogada_usuario = input("Pedra, papel ou tesoura? ")

jogada_pc = random.choice(jokenpo)
#computador = randit(0,2)
if jogada_usuario == jogada_pc:
    print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, jogue novamente!")
else:
    if jogada_usuario == 'pedra' and jogada_pc == 'papel':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, o computador ganhou!")
    elif jogada_usuario == 'pedra' and jogada_pc == 'tesoura':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, você ganhou!")
    elif jogada_pc == 'pedra' and jogada_usuario == 'papel':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, você ganhou!")
    elif jogada_pc == 'pedra' and jogada_usuario == 'tesoura':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, o computador ganhou!")
    elif jogada_usuario == 'papel' and jogada_pc == 'pedra':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, você ganhou!")
    elif jogada_usuario == 'papel' and jogada_usuario == 'tesoura':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, você ganhou!")
    elif jogada_pc == 'papel' and jogada_usuario == 'pedra':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, você ganhou!")
    elif jogada_pc == 'papel' and jogada_usuario == 'tesoura':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, o computador ganhou!")
    elif jogada_usuario == 'tesoura' and jogada_pc == 'pedra':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, o computador ganhou!")
    elif jogada_usuario == 'tesoura' and jogada_pc == 'papel':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, você ganhou!")
    elif jogada_pc == 'tesoura' and jogada_usuario == 'papel':
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, o computador ganhou!")
    else:
        print(f"Você jogou {jogada_usuario} e o computador {jogada_pc}, o computador ganhou!")


