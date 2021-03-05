#usuario deve digitar varios valores numericos e cadastre-os em uma lista.
# caso o numero ja esteja l;a, ele nao pode ser adicionado, no final
# todos os valores unicos digitados em ordem crescente
lista = []
n = 0
while n != '999':
    n = int(input("Digite um número, e digite 999 para parar: "))

    if n in lista:
        print("Esse número já foi adicionado. Tente novamente.")
    else:
        lista.append(n)
        print("número adicionado.")

print(lista)