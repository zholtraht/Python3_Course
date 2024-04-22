from random import randrange

n = randrange(0, 5)

print('''
Acabo de pensar em um numero inteiro de 0 a 5

Tentes adivinhar o numero escolhido:
''')

ne = int(input('Seu palpite... '))

if ne == n:
    print('ACERTOU!! Acabas de me vencer')
else:
    print(f'ERROU!! Minha esolha foi {n}')
