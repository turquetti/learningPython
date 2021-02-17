# leia varios numeros inteiro pelo teclado. o Programa só vai parar quando o usuario digitar o valor 999
# no final mostre quantos numeros foram diitados e qual foi a soma entre eles.

soma = contagem = n = 0

while n != 999:
    n = int(input("Digite um número: "))
    contagem += 1
    soma += n
print(f"A contagem foi de {contagem-1} números e a soma dos fatores é igual a {soma-999}")





