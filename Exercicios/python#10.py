din=float(input('Quanto dinheiro vocẽ tem na carteira? R$ '))
dolar= din / 5.105
euro= din / 5.2
print('Você pode comprar com R$ {:.2f} U$$ {:.4f} Dolar E$ {:.2f} Euros'.format(din, dolar, euro))
