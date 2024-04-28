#Crie um programa que:
#Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Cateto oposto... "))
ca = float(input("Cateto adjacente... "))

print(f"""
A hipotenusa vai medir {hypot(co, ca):.2f}.
""")
