#Escreva um programa que converta uma temperatura digitado em graus Celsius
# e converta para graus fahrenheit.

temp_c = float(input('Escreva uma temperatura em Celsius: '))
temp_f = (temp_c * 9/5) + 32
print('A temperatura em Fahrenheit será de {}F.'.format(temp_f))