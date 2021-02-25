#tenha uma tupla totalmente preenchida com uma contagem por extenso 
# de 0 até 20.
# seu programa deverá ler um numero pelo teclado entre 0 e 20 e mostra-lo por extenso.

contagem_usuario = int(input("Digite um número de 0 até 20: "))
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

for i in contagem: 
    if contagem_usuario >= 0 and contagem_usuario <= 20:
        numero = contagem[contagem_usuario]
    else:
        contagem_usuario = int(input("Número inválido. Digite um número de 0 até 20: "))

print(f"Você digitou o número {contagem_usuario}, esse número por extenso é assim: {numero}")