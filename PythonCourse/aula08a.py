import math
#1. (Ou) From math import sqrt, floor
num=int(input('Insere um número: '))
raiz=math.sqrt(num)
#2. (Ou) raiz = sqrt(num)
print(f'\nA raiz de {num} é igual a'
      f'\n{math.ceil(raiz)} arredondado para cima ,'
      #3. (Ou) {floor(raiz)}
      f'\n{math.floor(raiz)} arredondado para baixo e'
      f'\n{raiz:.2f} com duas casas decimais.')