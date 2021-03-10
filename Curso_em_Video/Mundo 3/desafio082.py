lista = []
n = 0
while n != 999:
    n = int(input("Digite um número e digite 999 para parar: "))
    lista.append(n)

par = []
impar = []
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(lista,par,impar)