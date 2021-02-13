#leia o ano de nascimento de 7 pessoas
#mostre quantas pessoas ja atingiram a maior idade 21
#e menor
maior_idade = 0
menor_idade = 0
for c in range(0,7):
    n = int(input("Digite o ano do seu aniversário: "))
    idade = 2021 - n

    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f"Há {maior_idade} pessoas maiores de idade e há {menor_idade} pessoas menores de idade.")
