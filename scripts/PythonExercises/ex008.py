'''
008. Escrever um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
# Pede ao utilizador para inserir um valor em metros
metros = float(input('Digite um valor em metros: '))

# Converte para outras unidades
decimetro = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

quilometro = metros / 1000
hectometro = metros / 100
decametro = metros / 10

# Mostra os resultados de forma mais organizada
print(f'{metros} metros é igual a:')
print(f'- {decimetro} decímetros')
print(f'- {centimetros} centímetros')
print(f'- {milimetros} milímetros')
print(f'- {decametro} decâmetros')
print(f'- {hectometro} hectômetros')
print(f'- {quilometro} quilômetros')
