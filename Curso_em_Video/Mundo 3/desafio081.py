lista = []
n = 0
while n != 999:
    n = int(input("Digite um número e digite 999 para parar: "))
    lista.append(n)

lista.sort(reverse=True)

print(lista)

print(lista)
if 5 in lista:
    print("O número 5 está na lista!")
else:
    print("O número 5 não está na lista")

print(f"Foram digitados o total de {len(lista)} números.")


