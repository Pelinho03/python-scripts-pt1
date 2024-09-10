# Pede ao utilizador para inserir a quantidade de Km percorridos
km_percorridos = float(input('Quantos Km foram percorridos com o carro? '))

# Pede ao utilizador para inserir o número de dias de aluguer
dias_alugados = int(input('Por quantos dias o carro foi alugado? '))

# Define os preços por dia e por Km percorrido
preco_por_dia = 52.0
preco_por_km = 0.50

# Calcula o custo total
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

# Mostra o resultado formatado
print('O total a pagar pelo aluguer do carro é de {:.2f}€'.format(custo_total))
