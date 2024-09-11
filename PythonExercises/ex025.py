'''
025. Criar um programa que leia o nome de uma pessoa e diga se ela tem “Silva” no nome.
'''
nome = input('Escreve o teu nome completo: ').strip()

# Verificar se o nome contém 'Silva'
print('silva' in nome.lower())
