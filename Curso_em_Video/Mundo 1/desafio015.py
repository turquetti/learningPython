# escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugados e quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60/dia e R$0,15/km.

km = float(input('Quantos kms foram rodados?'))
dia = float(input('Quantos dias o carro foi alugado?'))
total = dia*60 + km*0.15
print('O preço final será de R$ {:.2f} reais.'.format(total))