#Um dos professores quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto aluno: ")

turma = [n1, n2, n3, n4]

sorteio = random.choice(turma)
print(f"O aluno sorteado foi: {sorteio}")

