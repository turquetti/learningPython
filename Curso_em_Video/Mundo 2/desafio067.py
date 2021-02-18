#Mostre a tabuada de varios numeros. O programa será interrompido quando o noumero for negativo

while True:
    n = int(input("Digite o número que você gostaria de saber a tabuada: "))
    if n < 0:
        break
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
