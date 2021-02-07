#O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
#programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto aluno: ")

turma = [n1, n2, n3, n4]

random.shuffle(turma)

print(f"A ordem de apresentação será: {turma}")