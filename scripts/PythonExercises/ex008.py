'''
008. Escrever um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
# Pede ao utilizador para inserir um valor em metros
metros = float(input('Digite um valor em metros: '))

# Converte para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Mostra os resultados
print('{} metros é igual a {} centímetros e {} milímetros'.format(metros, centimetros, milimetros))
