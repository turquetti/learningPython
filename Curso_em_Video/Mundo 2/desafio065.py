# leia varios numeros inteiros, no final, mostre a media entre todos os valores e qual foi o maior e o menor. ele deve perguntar
#ao usuario se ele quer ou nao continuar a digitar os valores. 

maior = menor = media = 0

while n != 999:
    n = int(input("Digite um número: "))
    contagem += 1
    soma += n
print(f"A contagem foi de {contagem-1} números e a soma dos fatores é igual a {soma-999}")




