'''
033. Fazer um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
# Ler três números do utilizador
num1 = int(input('Introduza o primeiro número: '))
num2 = int(input('Introduza o segundo número: '))
num3 = int(input('Introduza o terceiro número: '))

# Encontrar o menor número
menor = min(num1, num2, num3)

# Encontrar o maior número
maior = max(num1, num2, num3)
1
# Mostrar o resultado
print(f'O menor número é {menor}.')
print(f'O maior número é {maior}.')
