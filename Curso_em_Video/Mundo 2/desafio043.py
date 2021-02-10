#leia o peso e altura de uma pessoa e calcule seu imc.
# abaixo de 18,5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 ate 30: Sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade mórbida

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso/(altura**2)

if IMC <= 18.5 and IMC <= 25: 
    print("Peso Ideal")
elif IMC <= 30:
    print("Sobrepeso")
elif IMC <= 40:
    print("Obesidade")
else: 
    print("Obesidade Mórbida")
