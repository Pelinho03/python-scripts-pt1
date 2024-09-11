# Perguntar o salário do funcionário
salario = float(input('Qual é o salário do funcionário? € '))

# Calcular o aumento com base no salário
if salario > 1250:
    aumento = salario * 0.10  # 10% de aumento para salários superiores a 1250€
else:
    aumento = salario * 0.15  # 15% de aumento para salários iguais ou inferiores a 1250€

# Novo salário após o aumento
novo_salario = salario + aumento

# Mostrar o aumento e o novo salário
print(f'O aumento será de €{aumento:.2f}.')
print(f'O novo salário será de €{novo_salario:.2f}.')
