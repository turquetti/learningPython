#Leia o ano de nascimento e informe conforme sua idade: 
# - Se ele ainda vai se alistar no exercito
# - Se é a hora de se alistar
# - Se ja passou do tempo do alistamento
#Deverá mostrar o tempo que falta ou que passou do prazo.

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

alistar = 2021 - ano_nascimento

if alistar == 18:
    print("Você já pode se alistar!")
elif alistar < 18:
    print(f"Você ainda não pode se alistar, faltam {18 - alistar} anos.")
else:
    print(f"Já passou da hora! Já se passaram {alistar - 18} anos.")
