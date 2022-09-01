# calulcar metragem da parede para ver quanto é necessário de tinta

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m2'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede você precisa de {} l de tinta'.format(tinta))

