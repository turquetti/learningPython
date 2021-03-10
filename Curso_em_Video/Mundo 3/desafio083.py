n = input("Digite uma frase usando parênteses: ")
a = '('
b = ')'

count_a = n.count(a)
count_b = n.count(b)

if count_a > 0 and count_b > 0:
    print("Parenteses estão fechados")
else:
    print("Parentesis abertos")