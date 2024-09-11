'''
030. Criar um programa que leia um número inteiro e mostre no ecrã se ele é PAR ou ÍMPAR.
'''
# Pedir ao utilizador para introduzir um número inteiro
numero = int(input('Escreva um número inteiro: '))

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é ÍMPAR.')
