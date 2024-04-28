#Faça um programa que:
#Leia um ângulo qualquer.
#Mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

from math import radians, sin, cos, tan

a = float(input("Ângulo... "))

print(f"""
O ângulo de {a} tem o seno de {sin(radians(a)):.2f}.
{'=' * 5}
O ângulo de {a} tem o cosseno de {cos(radians(a)):.2f}.
{'=' * 5}
O ângulo de {a} tem a tangente de {tan(radians(a)):.2f}.
""")
