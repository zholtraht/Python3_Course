#Crie um programa que:
#Leia o nome completo de uma pessoa.
#Exiba o nome com todas as letras maiúsculas.
#Exiba o nome com todas as letras minúsculas.
#Mostre quantas letras ao todo (sem considerar espaços).
#Mostre quantas letras tem o primeiro nome.

n = str(input("Nome completo... ")).strip()

print(f"""
Muito bem!! Vejamos...

Seu nome em maiúsculas é: {n.upper()}.
{'=' * 5}
Seu nome me minúsculas é: {n.lower()}.
{'=' * 5}
Seu nome possui {len(n) - n.count(' ')} letras.
{'=' * 5}
Seu primeiro nome possui {n.find(' ')} letras.
""")
