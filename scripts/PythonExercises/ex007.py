'''
007. Desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
# Pede ao utilizador para inserir as duas notas e nome
nome = input('Qual o nome? ')
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

# Calcula a média
media = (nota1 + nota2) / 2

# Mostra a média
print('O {} obteve as notas de {:.1f} e {:.1f} finalizando com média de {:.1f}'.format(nome,nota1, nota2, media))
