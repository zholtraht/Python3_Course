lp = float(input('Largura da parede...'))
ap = float(input('Altura da parede...'))
a = lp * ap
t = a / 2

print(f'''
Vejamos sua parede possui dimesao {lp:.0f}x{ap:.0f}, e area {a:.1f}m²

Para pitar essa parede, precisas de {t:.1f}l de tinta
''')
