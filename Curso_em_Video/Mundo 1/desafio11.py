#Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a 
# quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2 m2.

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
a = largura * altura
print('A quantidade de tinta necessária será um total de {} litros.'.format(a/2))