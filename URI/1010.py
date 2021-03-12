linha1 = input().split("")
linha2 = input().split("")

produto1, quantidade1, preco1 = linha1
produto2, quantidade2, preco2 = linha2

total = (int(quantidade1)*float(preco1)) + (int(quantidade2)*float(preco2))

print(f"VALOR A PAGAR: R$ {total:.2f}")