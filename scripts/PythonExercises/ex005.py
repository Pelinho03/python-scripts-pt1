'''
005. Criar um programa que leia um número inteiro e mostre no ecrã o seu sucessor e antecessor.
'''
# Pede ao utilizador para inserir um número inteiro
num = int(input('Digite um número inteiro: '))

# Calcula o sucessor e o antecessor
antecessor = num - 1
sucessor = num + 1

# Mostra o antecessor e o sucessor
print('O antecessor de {} é {} e o sucessor é {}'.format(num, antecessor, sucessor))

# Menor uso de variáveis, melhor desempenho
n2=int(input('Digita um número: '))
print('O valor {} tem como sucessor o número {} e antecessor o seguinte {}'.format(n2, (n2+1), (n2-1)))
