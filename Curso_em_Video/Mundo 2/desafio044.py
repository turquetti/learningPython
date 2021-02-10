#calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento.
#a vista dinheiro/cheque: 10%
#a vista no cartao: 5%
#em ate 2x no cartao: preco normal
# 3x ou mais no cartao: 20% de juros
valor = float(input("Digite o valor do produto: R$ "))

print("Formas de Pagamento:")
print("1. A vista no dinheiro/cheque")
print("2. A vista no cartão")
print("3. Em até 2x no cartão")
print("4. 3x ou mais no cartão")

pagamento = int(input("Qual será sua forma de pagamento? "))

if pagamento == 1:
    print(f"O valor final da compra será de {valor*0.9}") 
elif pagamento == 2:
    print(f"O valor final da compra será de {valor*0.95}") 
elif pagamento == 3:
    print(f"O valor final da compra será de {valor}") 
else: 
    print(f"O valor final da compra será de {valor + valor*0.2}") 