'''
016. Criar um programa que leia um número Real qualquer pelo teclado e mostre no ecrã a sua porção inteira. Ex.: 6.127, parte inteira 6.
'''
# Programa que lê um número real e mostra a sua parte inteira
import math

# Ler o número real
num = float(input("Digite um número real: "))

# Mostrar a parte inteira do número
print(f"A parte inteira de {num} é {math.trunc(num)}.")
