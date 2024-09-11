'''
026. Fazer um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra “A”;
- Em que posição ela aprece a primeira vez;
- Em que posição ela aprece a última vez.
'''
# Ler a frase e garantir que ela está em letras minúsculas para facilitar a contagem
frase = input('Escreve uma frase: ').strip().lower()

# Contar quantas vezes aparece a letra "a"
contagem_a = frase.count('a')

# Encontrar a posição da primeira ocorrência de "a" (somar 1 para corresponder ao número humano)
primeira_posicao = frase.find('a') + 1

# Encontrar a posição da última ocorrência de "a" (somar 1 para corresponder ao número humano)
ultima_posicao = frase.rfind('a') + 1

# Exibir os resultados
print(f'A letra "A" aparece {contagem_a} vezes na frase.')
print(f'A primeira letra "A" aparece na posição {primeira_posicao}.')
print(f'A última letra "A" aparece na posição {ultima_posicao}.')
