'''
017. Programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
'''
# Programa que calcula a hipotenusa de um triângulo retângulo
import math

# Ler o comprimento dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcular a hipotenusa usando o teorema de Pitágoras
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Mostrar o resultado
print(f"A hipotenusa é {hipotenusa:.2f}")