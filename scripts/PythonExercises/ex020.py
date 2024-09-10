'''
020. O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Fazer um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

# Ler o nome dos quatro alunos
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

# Colocar os nomes numa lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Baralhar a lista de alunos para definir a ordem de apresentação
random.shuffle(alunos)

# Mostrar a ordem sorteada
print('\nA ordem de apresentação dos trabalhos é:')
for i, aluno in enumerate(alunos, 1):
    print(f'{i}. {aluno}')
