from math import radians, sin, cos, tan

a = float(input('Angulo desejado...'))

print(f'''
O angulo de {a} tem o seno de {sin(radians(a)):.2f}
O angulo de {a} tem o cosseno de {cos(radians(a)):.2f}
O angulo de {a} tem a tangente de {tan(radians(a)):.2f}
''')
