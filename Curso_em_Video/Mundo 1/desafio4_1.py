#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 

objeto = input("Digite algo aqui: ")
print('O tipo primitivo desse valor é {}'.format(type(objeto)))
print('Só tem espaços? {}'.format(objeto.isspace()))
print('É um número? {}'.format(objeto.isnumeric()))
print('É alfabético? {}'.format(objeto.isalpha()))
print('É alfanumérico? {}'.format(objeto.isalnum()))
print('Está em maiúsculas? {}'.format(objeto.isupper()))
print('Está em minusculas? {}'.format(objeto.islower()))


# print(n.isnumeric()) #True if you type a number and False if not
# print(n.isalpha()) #alpha for text
# print(n.isalnum()) #alnum for alphanumeric - text and number
# print(n.isupper()) #for strings with uppercase
# print(n.islower()) #for strings with lowercase 