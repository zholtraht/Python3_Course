#Crie um programa que:
#Pergunte o salário de um funcionário.
#Calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.


s = float(input("""Quanto voce ganha?... """))
v1 = (s * 10 / 100) + s
v2 = (s * 15 / 100) + s

if s > 1250:
    print(f"""
    Passará a ganhar R${v1:.2f}.
    """)
else:
    print(f"""
    Passará a ganhar R${v2:.2f}
    """)
