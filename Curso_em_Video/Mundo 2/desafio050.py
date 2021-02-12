#que leia 6 numeros inteiros e mostre a soma 
#apenas daqueles que forem pares.

s = 0
for c in range(0,6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        s += n
print(s)
