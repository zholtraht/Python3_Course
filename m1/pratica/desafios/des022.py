n = str(input('Seu nome completo...')).strip()

print(f'''
Muito bem!! Vejamos...
Seu nome em maiusculas es: {n.upper()}
Seu nome me minusculas es: {n.lower()}
Seu nome possui {len(n) - n.count(' ')} letras
Seu primeiro nome possui {n.find(' ')} letras''')
