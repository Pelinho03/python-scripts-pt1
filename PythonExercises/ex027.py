'''
027. Fazer um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
- Ex.: Ana Maria de Souza
    - Primeiro = Ana
    - Último = Souza
'''
# Ler o nome completo e remover espaços extras
nome_completo = input('Escreve o teu nome completo: ').strip()

# Dividir o nome completo em partes
nomes = nome_completo.split()

# O primeiro nome é o primeiro elemento da lista
primeiro_nome = nomes[0]

# O último nome é o último elemento da lista
ultimo_nome = nomes[-1]

# Exibir o resultado
print(f'Primeiro nome = {primeiro_nome}')
print(f'Último nome = {ultimo_nome}')
