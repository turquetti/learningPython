#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# calcule e mostre o comprimento da hipotenusa.
import math
CO = float(input("Digite aqui o cateto oposto: "))
CA = float(input("Digite aqui o cateto adjacente: "))
H = (CO**2 + CA**2)**0.5
#H = math.hypot(CO,CA)
print(f"O comprimento da hipotenusa é de {H}")