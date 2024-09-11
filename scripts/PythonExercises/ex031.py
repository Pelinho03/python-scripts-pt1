'''
031. Desenvolver um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando 0,50€ por Km para viagens até 200Km e 0,45€ para viagens mais longes.
'''
# Pedir ao utilizador a distância da viagem em Km
distancia = float(input('Qual é a distância da viagem em Km? '))

# Calcular o preço da passagem
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Mostrar o preço da passagem
print(f'O preço da passagem para a viagem de {distancia} Km é {preco:.2f}€.')
