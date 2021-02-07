#Crie um programa que leia um número real qualquer pelo teclado e mostre na sua tela a sua porção inteira. 
import math
n = float(input("Digite aqui um número: "))
pi = math.trunc(n)
#print(f"A sua porção inteira é de {int(n)}")
print(f"A sua porção inteira é de {pi}")