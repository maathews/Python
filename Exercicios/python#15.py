km=float(input('Qual a quantidade de km percorridos? '))
dias=int(input('Qual a quantidade de dias alugados? '))
diaria= dias * 60
rodado= km * 0.15
total= diaria + rodado
print('O total de diarias é R$ {} e o valor de Km é {:.2f} o total é de R$ {:.2f} '.format(diaria,rodado,total))
