lista = []
n = 0 

for i in range(0,5):
    n = int(input("Digite um número: "))

    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        position = 0
        while position < len(lista):
            if n <= lista[position]:
                lista.insert(position, n)
                break
            position =+ 1

print(lista)
