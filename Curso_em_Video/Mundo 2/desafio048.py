#calcule a soma entre todos os numeros impares
#que sao multiplos de tres e que se encontram no intervalo
#de 1 ate 500
s = 0
for c in range(1,500):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print(s)       

