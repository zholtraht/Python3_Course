a = int(input('Em que ano estamos?... '))
cb = a % 4
cb1 = a % 100
cb2 = a % 400

if cb == 0 and cb1 != 0 or cb2 == 0:
    print(f'''BISSEXTO''')
else:
    print(f'''NAO BISSEXTO''')
