#Escreva um programa que leia a velocidade do carro. Se ele ultrapassar 80km/h,
#Mostre uma mensagem dizendo que ele foi multado. a multa vai custar 7 reais por cada km acima do limite.
vel = float(input("Digite a velocidade em km: "))

if vel > 80:
    multa = (vel - 80)*7
    print(f"Você foi multado! Sua multa será no valor de R${multa}")
else:
    print("Tá liberado!")