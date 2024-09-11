'''
029. Escrever um programa que leia a velocidade de um carro. Se estiver acima de 80Km/h, mostra uma mensagem de Multa. A multa vai custar 10€ por cada Km acima do limite.
'''
# Pedir a velocidade do carro
velocidade = float(input('Qual é a velocidade atual do carro em Km/h? '))

# Limite de velocidade
limite = 80

# Verificar se a velocidade está acima do limite
if velocidade > limite:
    # Calcular o valor da multa
    excesso = velocidade - limite
    multa = excesso * 10
    print(f'Estás multado! Excedeste o limite de {limite}Km/h porque ias a {velocidade:.0f}Km/h.')
    print(f'Terás de pagar uma multa de {multa:.2f}€ por excesso de velocidade.')
else:
    print('Estás dentro do limite de velocidade. Continua a conduzir com segurança!')
