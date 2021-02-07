#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input("Digite o seu nome completo: ").strip()
res = 'Silva' in nome
print(f"Seu nome tem Silva? {res}")