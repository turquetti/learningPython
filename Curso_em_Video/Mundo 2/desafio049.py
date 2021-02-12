#Refaça o desaio 9 mostrando a tabuada de um numero com o loop
 
n = int(input('Digite um número: '))

for c in range(1,11):
    print('{} x {} = {}'.format(n, c, n*c))

