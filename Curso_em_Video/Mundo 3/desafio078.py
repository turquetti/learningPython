#Leia 5 valores e guarde-os em uma lista.
# No final mostre qual foi o maior e o menor valor digitado e as suas posições na lista
maior = menor =  0
lista = []

for i in range(0,5):
    n = int(input("Digite um número: "))
    lista.append(n)
    
    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(lista, maior, menor)
print(f"O maior número digitado foi: {maior} na posição {lista.index(maior)} e o menor foi {menor} na posição {lista.index(menor)}")

