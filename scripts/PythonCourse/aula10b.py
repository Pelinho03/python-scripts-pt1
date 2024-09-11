n1 = float(input('Digita a 1ª nota: '))
n2 = float(input('Gigita a 2ª nota: '))
m = (n1 + n2) / 2
print(f'A tua média foi {m:.1f}')
if m >= 6.0:
    print('Boa média! PARABÉNS!')
else:
    print('Média baixa! ESTUDAR MAIS!')
print('PARABÉNS!' if m >= 6 else 'ESTUDAR MAIS!')
