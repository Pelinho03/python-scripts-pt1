'''
012. Fazer um algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto.
'''
# Pede ao utilizador para inserir o preço do produto
preco = float(input('Digite o preço do produto: '))

# Calcula o desconto de 5%
desconto = preco * 0.05

# Calcula o novo preço com desconto
preco_com_desconto = preco - desconto

# Mostra o preço original e o preço com desconto
print('O preço original do produto é {:.2f}€'.format(preco))
print('Com 5% de desconto, o novo preço é {:.2f}€'.format(preco_com_desconto))
