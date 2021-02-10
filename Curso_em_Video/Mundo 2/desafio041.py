# A confederação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a sua idade:
# ate 9 anos: mirim
# ate 14: infantil
# ate 19; junior
# ate 20: senior
#acima: master

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano = 2021 - ano_nascimento

if ano <= 9:
    print("Mirim")
elif ano <= 14:
    print("Junior")
elif ano <= 19:
    print("Junior")
elif ano <= 20:
    print("Senior")
else: 
    print("Master")