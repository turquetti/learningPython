#Crie um programa que leia duas notas de um aluno e calcule sua média.
# - media abaixo de 5: reprovado
# - media entre 5 e 6,9: recuperação
# - media 7 ou superior: Aprovado

nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))

media = (nota1 + nota2)/2

if media < 5:
    print("Reprovado!")
elif media >= 5 and media < 7:
    print("Recuperação!")
else:
    print("Aprovado!")