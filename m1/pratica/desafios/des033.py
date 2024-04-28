#Crie um programa que:
#Leia três números.
#Mostre qual é o maior e qual é o menor.

n1 = int(input("Um número... "))
n2 = int(input("Outro número... "))
n3 = int(input("Outro número... "))

if n1 < n2 and n1 < n3:
    me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3

if n1 > n2 and n1 > n3:
    ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3

print(f"""
MAIOR: {ma}.
{'=' * 5}
MENOR: {me}.
""")
