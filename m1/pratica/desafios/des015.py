qd = int(input('Quatos dias alugados?... '))
qk = float(input('Quantos km rodados?... '))
v = qd * 60 + qk * 0.15

print(f'''
O total a pagar e R${v:.2f}
''')
