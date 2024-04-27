#Faça um programa que:
#Leia algo pelo teclado.
#Mostre na tela o seu tipo primitivo.
#Mostre todas as informações possíveis sobre ele.

v = input("Digite algo... ")

print(f"""
Vejamos... você digitou {v}.

Tipo primitivo: {type(v)}.
{'=' * 15}
Está numérico? {v.isnumeric()}.
{'=' * 15}
Está alfabético? {v.isalpha()}.
{'=' * 15}
Está alfanumérico? {v.isalnum()}.
{'=' * 15}
Estão somente espaços? {v.isspace()}.
{'=' * 15}
Estão somente maiúsculas? {v.isupper()}.
{'=' * 15}
Estão somente minusculas? {v.islower()}.
{'=' * 15}
Está capitalizado? {v.istitle()}.
""")
