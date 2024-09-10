'''
022. Criar um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome.
'''
# Ler o nome completo do utilizador
nome_completo = input("Digite o seu nome completo: ").strip()

# Exibir o nome com todas as letras maiúsculas
print(f"Nome em maiúsculas: {nome_completo.upper()}")

# Exibir o nome com todas as letras minúsculas
print(f"Nome em minúsculas: {nome_completo.lower()}")

# Calcular o número de letras sem considerar os espaços
num_letras = len(nome_completo.replace(" ", ""))
print(f"Total de letras (sem espaços): {num_letras}")

# Encontrar o primeiro nome e calcular o número de letras
primeiro_nome = nome_completo.split()[0]
print(f"O primeiro nome é '{primeiro_nome}' e tem {len(primeiro_nome)} letras.")
