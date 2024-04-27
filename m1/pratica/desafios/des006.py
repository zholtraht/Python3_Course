#Crie um programa que:
#Leia um número.
#Mostre o seu dobro, triplo e raiz quadrada.


n = int(input("Um número... "))
d = (n * 2)
t = (n * 3)
r = n ** (1/2)

print(f"""
Vejamos…

você digitou {n}.

Seu dobro é: {d}.
{'=' * 10}
seu triplo é: {t}.
{'=' * 10}
sua raiz quadrada é: {r:.1f}.
""")
