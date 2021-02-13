#nome, idade, sexo de 4 pessoas, deve mostrar a media de idade,
#qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
soma_idades = 0
qtd_mulheres = 0
idade_masc = 0
nome_masc = ""

for c in range(0,4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")

    soma_idades += idade

    if sexo == 'F' and idade <= 20:
        qtd_mulheres += 1
    
    if sexo == 'M':
        if idade > idade_masc:
            idade_masc = idade
            nome_masc = nome


media = soma_idades/4

print(soma_idades, media, qtd_mulheres,nome_masc)