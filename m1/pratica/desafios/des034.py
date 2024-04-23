s = float(input('Quanto voce ganha?... '))
v1 = (s * 10 / 100) + s
v2 = (s * 15 / 100) + s

if s > 1250:
    print(f'''Passara a ganhar R${v1:.2f}''')
else:
    print(f'''Passara a ganhar R${v2:.2f}''')
