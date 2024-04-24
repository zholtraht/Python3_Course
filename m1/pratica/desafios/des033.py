n1 = int(input('Digite um numero... '))
n2 = int(input('Digite outro numero... '))
n3 = int(input('Outro numero... '))

if n1 < n2 and n1 < n3:
    me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3

if n1 > n2 and n1 > n3:
    ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3

print(f'''
MAIOR: {ma}
MENOR: {me}
''')
