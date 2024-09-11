'''
013. Fazer um algoritmo que leia o salário de um funcionário e mostre o novo salário, com 15% de aumento.
'''
# Pede ao utilizador para inserir o salário do funcionário
salario = float(input('Digite o salário do funcionário (em €): '))

# Calcula o aumento de 15%
aumento = salario * 0.15

# Calcula o novo salário com aumento
novo_salario = salario + aumento

# Mostra o salário original e o novo salário com aumento
print('O salário original do funcionário é €{:.2f}'.format(salario))
print('Com 15% de aumento, o novo salário é €{:.2f}'.format(novo_salario))
