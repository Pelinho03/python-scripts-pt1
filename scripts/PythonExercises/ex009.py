'''
009. Fazer um programa que leia um número inteiro qualquer e mostre no ecrã a sua tabuada.
'''
# Pede ao utilizador para inserir um número inteiro
num = int(input('Indica um número inteiro: '))

# Ciclo for para gerar a tabuada
for i in range(1, 11):  # Gera os números de 1 a 10
    valor = num * i
    print('{} x {} = {}'.format(num, i, valor))
