import math
cateto=float(input('Qual o comprimento cateto oposto: '))
adja=float(input('Qual o comprimento cateto adjacente: '))
hipo= math.hypot(cateto,adja)                     
print('A hipotenusa é {:.2f} '.format(hipo))
