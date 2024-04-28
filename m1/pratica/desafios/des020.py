#"Um professor quer sortear a ordem de apresentação de trabalhos dos alunos."

#Crie um programa que:
#Leia o nome dos quatro alunos.
#Mostre a ordem sorteada.

from random import shuffle

pa = str(input("Primeiro aluno... "))
sa = str(input("Segudo aluno... "))
ta = str(input("Terceiro aluno... "))
qa = str(input("Quarto aluno... "))

l = [pa, sa, ta, qa]

rs = shuffle(l)

print(f"""
A ordem de apresentação será:

1. {l[0]}.
2. {l[1]}.
3. {l[2]}.
4. {l[3]}.
""")
