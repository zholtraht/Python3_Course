#Crie um programa que:
#Leia o nome completo de uma pessoa.
#Mostre o primeiro e o último nome separadamente. 

n = str(input("Nome completo... ")).strip().lower().title()
ns = n.split()

print(f"""
Muito prazer, {n}!!

Seu primeiro nome é {ns[0]}.
{'=' * 5}
Seu ultimo nome é {ns[len(ns)-1]}.
""")
