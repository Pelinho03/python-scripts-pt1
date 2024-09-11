a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor foi {menor}.')
print(f'O maior valor foi {maior}.')
