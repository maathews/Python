preço = float(input('Qual o preço do produto?R$ '))
desconto = float(input('Qual o desconto que deseja dar ao produto em %: '))
novo = preço - (preço * desconto / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de: {:.1f} % vai custar R$ {:.2f}'.format(preço, desconto, novo))
