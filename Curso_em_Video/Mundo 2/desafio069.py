# Leia idade, sexo de varias pessoas. O programa deve perguntar ao usuario se ele quer ou nao continuar. No final mostre
# quantas pessoas tem mais de 18, quantos homens, quantas mulheres tem menos de 20 anos.

i_18 = i_homens = i_mulheres = 0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: [M/F] ")
    cont = input("Deseja continuar? [S/N] ")
    
    if cont == 'N':
        break
    if idade >= 18:
        i_18 += 1
    if sexo == 'M':
        i_homens += 1
    if sexo == 'F' and idade <= 20:
        i_mulheres += 1

print(f'''
Você registrou:
[{i_18}] pessoas maiores de 18 anos;
[{i_homens}] homens;
[{i_mulheres}] mulheres com idades inferiores a 20 anos.
''')