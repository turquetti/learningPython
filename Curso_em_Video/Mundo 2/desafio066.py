#Leia vários numeros inteiros. O programa só vai parar quando o usuario digitar 999.
# Mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando o flag.

i = s = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 999:
        break
    s += n
    i += 1
print(f"Foram computados {i} números e a soma deles é igual a {s}.")
