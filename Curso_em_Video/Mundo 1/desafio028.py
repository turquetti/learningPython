#Escreva um programa que faça o computador pensar num numero inteiro
#Entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido
#pelo computador. O programa devera escrever na tela se o usuario acertou ou nao.
import random 
n_usuario = int(input("Digite um número entre 0 e 5: "))
n_pc = random.randint(0,5)

if n_usuario == n_pc:
    print("Parabéns, você acertou!")
else:
    print("Não foi dessa vez!")
