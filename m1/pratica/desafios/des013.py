s = float(input('Salario atual de um funcionario... R$'))
sa = s + (s * 15 / 100)

print(f'''
O salario de um funcionario que ganha R${s:.2f}, com 15% de aumento passa a ser {sa:.2f}
''')
