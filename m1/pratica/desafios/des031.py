km = float(input('Digite um valor em quilometros... '))
v1 = (km * 0.50)
v2 = (km * 0.45)

if km > 200:
    print(f'''R${v2:.2f}''')
else:
    print(f'''R${v1:.2f}''')
