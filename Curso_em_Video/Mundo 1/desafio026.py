#Crie um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A
#Em que posição ela aparece pela primeira vez
#em que posição ela aparece a ultima vez

frase = input("Escreva uma frase aqui: ").strip().lower()
contagem = frase.count('a')
print(f"A letra 'a' aparece {contagem} vezes.")
posicao_inicio = frase.find('a')+1
print(f"A letra 'a' aparece pela primeira vez na posição {posicao_inicio}.")
posicao_fim = frase.rfind('a')+1
print(f"A letra 'a' aparece pela última vez na posição {posicao_fim}.")