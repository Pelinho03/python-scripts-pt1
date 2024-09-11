'''
015. Escrever um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcular o preço a pagar, sabendo que o carro custa 52€ por dia e 0,50€ por Km rodado.
'''
km = float(input('Quantos quilómetros percorreste? '))
dias = int(input('Por quantos dias? '))

precodias = dias * 52
precokm = km * 0.50

precofinal = precodias + precokm

# Mostra o resultado formatado com duas casas decimais
print(f'\nPercorreste {km}Km em {dias} dias.\nDá um total de {precofinal:.2f}€.')