#crie um programa que leia o nome completo de uma pessoa e mostre;
#o nome com todas as letras maiusculas.
#o nome com todas as letras minusculas.
#Quantas letras ao todo (sem considerr os espaços)
#Quantas letras tem o primeiro nome.

nome = input("Digite aqui seu nome completo: ")
print(f"O seu nome completo em letras maiusculas é {nome.upper()}")
print(f"O seu nome completo em letras minusculas é {nome.lower()}")
contagem = len(nome) - nome.count(' ')
print(f"O seu nome completo tem {contagem} letras.")
primeiro = nome.split()
print(f"Seu primeiro nome tem {(len(primeiro[1]) - 1)} letras.") 
#nome.find(' ')