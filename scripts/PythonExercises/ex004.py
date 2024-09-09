'''
004. Criar um programa que leia algo pelo teclado e mostre no ecrã o seu tipo primitivo e todas as informações possíveis sobre ele.
'''
# Pede ao utilizador para inserir algo
valor = input('Escreve algo: ')

# Mostra o tipo primitivo do valor
print('O tipo primitivo desse valor é', type(valor))

# Mostra informações adicionais sobre o valor
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizado?', valor.istitle())  # Verifica se está com a primeira letra maiúscula e o resto minúsculo
