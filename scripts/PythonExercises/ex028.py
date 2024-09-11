'''
028. Escrever um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o utilizador tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever no ecrã se o utilizador venceu ou perdeu.
'''
import random
import time

# Computador "pensa" num número entre 0 e 5
numero_computador = random.randint(0, 5)

# Pedir ao utilizador para tentar adivinhar o número
print('Vou pensar num número entre 0 e 5... tenta adivinhar!')
numero_utilizador = int(input('Qual número achas que escolhi? '))

# Simulação de "processamento"
print('A processar...')
time.sleep(2)  # Aguarda 2 segundos para simular que está a "pensar"

# Verificar se o utilizador acertou
if numero_utilizador == numero_computador:
    print(f'Parabéns! Acertaste, eu escolhi o número {numero_computador}.')
else:
    print(f'Que pena! Eu escolhi o número {numero_computador} e não {numero_utilizador}.')
