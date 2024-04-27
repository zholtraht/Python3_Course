#Crie um um programa que:
#Leia as duas notas de um aluno.
#Calcule e mostre a sua média.

n1 = float(input("Uma nota... "))
n2 = float(input("Outra nota... "))
m = (n1 + n2) / 2

print(f"""
Vejamos...

Suas notas foram {n1:.1f} e {n2:.1f}.

Sua média é {m:.1f}.
""")
