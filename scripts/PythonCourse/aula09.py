frase='Manipulação de textos.'
print(frase)
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase.strip()))
nova_frase=frase.replace('textos', 'Python')
print(frase)
print(nova_frase)
print('textos' in frase)
print(frase.find('textos'))
dividida=frase.split()
print(dividida[0][3])


print("""\nThe standard chunk of Lorem Ipsum used
since the 1500s is reproduced below for those interested. 
Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" 
by Cicero are also reproduced in their exact original form, 
accompanied by English versions from the 1914 translation by H. Rackham.""")