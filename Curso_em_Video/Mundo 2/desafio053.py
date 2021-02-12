#leia uma frase e diga se é um palindromo, desconsidando os espaços

frase = input("Digite uma frase e descubra se ela é um palindromo: ").lower()

frase_s_espaco = frase.replace(" ", "")

aux = ""
for c in range(0, len(frase_s_espaco)):
    aux += frase_s_espaco[c]

if aux == aux[::-1]:
    print("É palindromo")
else:
    print("Não é palindromo")
