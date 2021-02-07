#Pergunte a distancia de uma viagem em km. Calcule o preço da passagem cobrando 0,50/km
# para viagens ate 200km e 0,45 para viagens mais longas.

n = float(input("Digite a quantidade de km percorridos: "))

if n <= 200:
    print(f"O valor da sua viagem será de R$ {n*0.5} reais.")
else:
    print(f"O valor da sua viagem será de R$ {n*0.45} reais.")