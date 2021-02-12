#leia o primeiro termo e a razao de uma PA.
#mostre os 10 primeiros termos da PA

termo_pa = int(input("Digite o termo da PA: "))
razao_pa = int(input("Digite a razao da PA: "))

for c in range(1,10):
    pa = termo_pa + (c - 1) * razao_pa
    print(pa)