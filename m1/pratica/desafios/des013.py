#Crie um programa que:
#Leia o salário de um funcionário.
#Mostre seu novo salário, com 15% de aumento.

s = float(input("Salário atual de um funcionário... R$"))
sa = s + (s * 15 / 100)

print(f"""
Vejamos...
O funcionário que ganha R${s:.2f}.
Com 15% de aumento passa a ganhar R${sa:.2f}.
""")
