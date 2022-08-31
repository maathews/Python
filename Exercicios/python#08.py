medida = float(input('Uma distância em metros: '))
km= medida / 100
dm= medida / 100
cm = medida * 100
mm = medida * 1000
print('A medida de {} m corrêsponde a {:.0f} cm e {:.0f} mm {:0f} dm {:0f} km'.format(medida, cm, mm, dm, km))
