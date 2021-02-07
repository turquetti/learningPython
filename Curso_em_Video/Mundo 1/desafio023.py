#Faça um programa que leia um numero de 0 a 9999 e mostre
#na tela cada um dos digitos separados.
# Ex. 1834
# unidade:4
# dezena:3
# centena:8
# milhar:1

n = int(input("Digite um número entre 0 e 9999: "))
unidade = n % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print(f"unidade: {unidade}, dezena: {dezena}, centena: {centena}, milhar: {milhar}")
