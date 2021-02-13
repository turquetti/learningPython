#leia o peso de 5 pessoas e mostre qual foi o menor e maior peso. 
maior = 0
menor = 0

for i in range(0,3):
    n = float(input("Digite o seu peso: "))

    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(maior, menor)