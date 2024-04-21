n = str(input('Seu nome completo...')).strip().lower().title()
ns = n.split()

print(f'''
Muito prazer, {n}!
Seu primeiro nome e {ns[0]}
Seu ultimo nome e {ns[len(ns)-1]}
''')
