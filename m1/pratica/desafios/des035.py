r1 = float(input('Primeiro segmento... ')) 
r2 = float(input('Seundo segmento... '))
r3 = float(input('Terceiro segmento... '))

c1 = (r2 + r3)
c2 = (r1 + r3)
c3 = (r1 + r2)

if r1 < c1 and r2 < c2 and r3 < c3:
    print('''Um triangulo PODE ser formado... ''')
else:
    print('''Um triangulo NAO PODE ser formado... ''')
