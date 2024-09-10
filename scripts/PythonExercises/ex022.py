'''
022. Criar um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome.
'''
nome=input('Insere o teu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome))

dividida=nome.split()
print(len(dividida[0]))