#Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e ultimo nome separadamente
#Ex. Ana maria de souza
#Primeiro: Ana
#Ultimo: Souza

nome = input("Digite seu nome completo: ")
n = nome.split()
print(f"Primeiro: {n[0]} \nUltimo: {n[len(n)-1]} ")