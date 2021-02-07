#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n = float(input("Digite aqui um ângulo: "))
rad = math.radians(n)
sen, cos, tg = math.sin(rad), math.cos(rad), math.tan(rad)
print(f"Seno é de {sen:.2f}, Cosseno é de {cos:.2f} e tangente de {tg:.2f}")