'''
010.  Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
'''
# Pede ao utilizador para inserir a quantidade de euros
euros = float(input('Quanto dinheiro tens na carteira (em €)? '))

# Define a taxa de câmbio (exemplo: 1 euro = 1.10 dólares)
taxa_cambio = 1.10

# Calcula a quantidade em dólares
dolares = euros * taxa_cambio

# Mostra o valor em dólares
print('Com €{:.2f}, podes comprar ${:.2f} dólares.'.format(euros, dolares))
