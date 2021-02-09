#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#O prorama vai perguntar o valor da casa, o salario do comptrador e em quantos anos ele vai pagar.
#Calcule o valor da prestaçào mensal, sabendo que ela não pode exceder 30% do salario ou então o 
#empréstimo será negado. 
valor_casa = float(input("Digite o valor da casa: R$ "))

salario = float(input("Qual é o seu salário? R$ "))

anos = int(input("Quer pagar em quantos anos? "))

prestacao = valor_casa/(anos*12)

print(f"Para pagar uma casa de R$ {valor_casa} em {anos} anos, a prestação será de R$ {prestacao} reais.")
if prestacao > salario*0.3:
    print("Me desculpe, seu empréstimo foi negado.")
else: 
    print("Emprestimo aprovado!.")


