# Jogue par ou impar com o computador, o jogo só sera interrompido quando o jogador perder. 
# E mostre quantas jogadas vc fez ate perder.

import random
lista = ['P', 'I']
c = 0
while True:
    resposta_usuario = input("Par ou Impar? [P/I]: ")
    resposta_computador = lista[random.randrange(0,1)]
    
    if resposta_usuario != resposta_computador:
        break
    c += 1

print(f"Você perdeu! Você ganhou {c} do computador.")