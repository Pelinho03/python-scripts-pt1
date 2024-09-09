'''
011.  Fazer um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
'''
# Pede ao utilizador para inserir a largura e a altura da parede
largura = float(input('Largura da parede (em metros): '))
altura = float(input('Altura da parede (em metros): '))

# Calcula a área da parede
area = largura * altura

# Cada litro de tinta cobre 2 metros quadrados
litros_tinta = area / 2

# Mostra a área e a quantidade de tinta necessária
print('A área da parede é de {:.2f} m²'.format(area))
print('Para pintar esta parede, vais precisar de {:.2f} litros de tinta.'.format(litros_tinta))
