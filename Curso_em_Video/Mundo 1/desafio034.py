#Aumento salario. >1250 aumento de 10%
#<= 1250 aumento de 15%

salario = float(input("Digite seu salário: "))
if salario > 1250:
    print(f"O seu salário novo será de {salario+salario*0.1}")
else: 
    print(f"O seu salário novo será de {salario+salario*0.15}")