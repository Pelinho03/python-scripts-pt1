'''
023. Fazer um programa que leia um número de 0 a 9999 e mostre no ecrã um dos dígitos separados.
- Ex.: Número 1834
    - Unidade: 4
    - Dezena: 3
    - Centena: 8
    - Milhar: 1
'''
# Ler um número entre 0 e 9999
numero = int(input("Digite um número entre 0 e 9999: "))

# Separar os dígitos do número
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Exibir os resultados
print(f"Analisando o número {numero}:")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
