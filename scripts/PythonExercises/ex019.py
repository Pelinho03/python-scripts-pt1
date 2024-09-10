'''
019. Um professor quer sortear um dos quatro alunos para apagar o quadro. Fazer um programa que ajude nisso, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random

# Ler o nome dos quatro alunos
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

# Colocar os nomes numa lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sortear um aluno
escolhido = random.choice(alunos)

# Mostrar o nome do aluno escolhido
print(f'O aluno escolhido para apagar o quadro é: {escolhido}')
