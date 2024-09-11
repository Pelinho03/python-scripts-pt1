'''
018. Programa que leia um ângulo qualquer e mostre no ecrã o valor do seno, cosseno e tangente desse ângulo.
'''
import math

# Ler o ângulo do utilizador
angulo = float(input('Indica um ângulo em graus: '))

# Converter o ângulo para radianos
angulo_rad = math.radians(angulo)

# Calcular o seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Mostrar os resultados
print(f'O ângulo de {angulo} graus tem:')
print(f' - Seno: {seno:.2f}')
print(f' - Cosseno: {cosseno:.2f}')
print(f' - Tangente: {tangente:.2f}')
