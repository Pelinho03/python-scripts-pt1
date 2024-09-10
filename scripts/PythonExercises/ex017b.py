import math

c_oposto=float(input('Indica a medida do cateto oposto: '))
c_adjacente=float(input('Agora a medida para o cateto adjacente: '))

hipotenusa= math.sqrt(pow(c_oposto,2)+pow(c_adjacente,2))

print(f'\nO cateto oposto é {c_oposto} e o cateto adjacente è {c_adjacente}'
      f'\no que dá como hipotenusa {hipotenusa:.2f}')