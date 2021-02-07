#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"

cidade = input("Digite o nome da cidade: ").strip().lower()
res = 'Santo' in cidade
print(f"A {cidade} começa com Santo? {res}")