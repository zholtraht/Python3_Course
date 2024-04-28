#Crie um programa que:
#Leia um número de 0 a 9999.
#Mostre na tela cada um dos dígitos separados.

n = int(input("Um número... "))
u = (n // 1 % 10)
d = (n // 10 % 10)
c = (n // 100 % 10)
m = (n // 1000 % 10)

print(f"""
Vejamos... Você digitou {n}.

Unidade: {u}.
{'=' * 5}
Dezena: {d}.
{'=' * 5}
Centena: {c}.
{'=' * 5}
Milhar: {m}.
""")
