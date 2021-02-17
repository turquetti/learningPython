# leia um numero e mostre seu fatorial

from math import factorial

n = int(input("Digite um número para descobrir seu fatorial: "))
f = factorial(n)
print(f)

n = int(input("Digite um número para descobrir seu fatorial: "))
c = n
f = 1
while c > 0:
    f *= c
    c -=1