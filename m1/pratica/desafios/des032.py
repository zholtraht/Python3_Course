a = int(input('Em que ano estamos?... '))
cb = a % 4

if cb == 0:
    print(f'''BISSEXTO''')
else:
    print(f'''NAO BISSEXTO''')
