n1 = int(input("Um numero... "))
n2 = int(input("Outro numero... "))

if n1 > n2:
    print(
f"""
O primeiro valor ({n1}) e maior.
""")

elif n1 < n2:
    print(
f"""
O segundo valor ({n2}) e maior.
""")

else:
    print(
"""
Ambos os valores sao iguais.
""")
