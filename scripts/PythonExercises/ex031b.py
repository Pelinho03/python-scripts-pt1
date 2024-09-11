dis = float(input('Qual a distância? '))
print(f'Estás prestes a começar uma viagem de {dis}Km.')
preco = dis * 0.5 if dis <= 200 else dis * 0.45
print(f'E o preço da passagem será de {preco:.2f}€.')
