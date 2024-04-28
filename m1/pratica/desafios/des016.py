#Crie um programa que:
#Leia um número Real qualquer pelo teclado.
#Mostre na tela a sua porção Inteira.

from math import trunc

n = float(input("Digite um valor... "))

print(f"""
Muito bem!!

Você digitou {n}. Seu valor inteiro é {trunc(n)}.
""")
