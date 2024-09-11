'''
032. Fazer um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
# Pedir ao utilizador para introduzir um ano
ano = int(input('Introduza um ano: '))

# Verificar se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
