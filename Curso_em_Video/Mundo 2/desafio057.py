# leia o sexo de uma pessoa mas só aceite os valores "M" e "F", caso esteja errado, peça a 
# digitação novamente até ter um valor correto. 
n = input("Digite o seu sexo: ")
while n not in 'MmFf':
    n = input("Por favor, tente novamente. Digite o seu sexo: ")
print("FIM")    

