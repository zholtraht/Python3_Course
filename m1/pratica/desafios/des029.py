vc = float(input('Velocidade do carro... '))
vm = (vc - 80) * 7

if vc > 80:
    print(f'''Multado!!
voce estava a {vc - 80}km acima da velocidade permitida
Sera multado em R${vm}''')
    
else:
    print('''
Tudo em ordem... ''')
