'''
034. Escrever um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1.250,00€, calcula o aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.
'''
salario=float(input('Digita o salário do funcionário: '))

if salario > 1250:
    aumento=salario*1.10
    print(f'O salário {salario}€ com aumento de 10% passa a ser de {aumento:.2f}€.')
elif salario<=1250:
    aumento=salario*1.15
    print(f'O salário {salario}€ com aumento de 15% passa a ser de {aumento:.2f}€.')