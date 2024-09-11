'''
024. Criar um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.
'''
# Ler o nome da cidade
cidade = input('Escreve o nome da cidade: ').strip()

# Verificar se começa com "SANTO" (independente de maiúsculas/minúsculas)
comeca_com_santo = cidade.upper().startswith('SANTO')

# Mostrar o resultado
if comeca_com_santo:
    print('A cidade começa com "SANTO".')
else:
    print('A cidade não começa com "SANTO".')
