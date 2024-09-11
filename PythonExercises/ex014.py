'''
014. Criar um programa que converte uma temperatura em graus Celsius para graus Fahrenheit.
'''
# Pede ao utilizador para inserir a temperatura em graus Celsius
celsius = float(input('Adiciona uma temperatura em ºC: '))

# Converte a temperatura de Celsius para Fahrenheit
# Fórmula: Fahrenheit = (Celsius * 1.8) + 32 ou (Celsius * 9/5) + 32
fahrenheit = (celsius * 1.8) + 32

# Mostra o resultado com formatação, usando a função format()
print('A temperatura {:.2f}ºC são {:.2f}ºF.'.format(celsius, fahrenheit))

# Mostra o resultado usando f-string (forma mais moderna e simples de formatação)
print(f'{celsius}ºC é igual a {fahrenheit}ºF')
