'''
035. Desenvolver um programa que leia o comprimento de três retas e diga ao utilizador se elas podem ou não formar um triângulo.
'''
# Leitura dos comprimentos das três retas
r1 = float(input('Indica o comprimento da primeira reta: '))
r2 = float(input('Indica o comprimento da segunda reta: '))
r3 = float(input('Indica o comprimento da terceira reta: '))

# Verificar se as três retas podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas NÃO podem formar um triângulo.')
