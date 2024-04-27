#Faça um programa que:
#Leia um número Inteiro.
#Mostre na tela o seu sucessor e seu antecessor.

n = int(input("Um número... "))
a = (n - 1)
s = (n + 1)

print(f"""
Vejamos…

você digitou {n}.

Seu sucessor é {s}, e seu antecessor é {a}.
""")
