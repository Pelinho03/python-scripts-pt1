'''
006.  Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
# Pede ao utilizador para inserir um número
num = int(input('Digite um número: '))

# Calcula o dobro, triplo e raiz quadrada
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5  # ou também podes usar a função pow(num, 0.5)

# Mostra os resultados
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(num, dobro, triplo, raiz_quadrada))
