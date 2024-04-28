#"Um professor vai sortear um dos seus quatro alunos para apagar o quadro"

#Crie um programa que:
#Leia o nome dos alunos.
#Escreva na tela o nome do escolhido.

from random import choice

pa = str(input("Primeiro aluno... ")).upper()
sa = str(input("Segundo aluno... ")).upper()
ta = str(input("Terceiro aluno... ")).upper()
qa = str(input("Quarto aluno... ")).upper()

l = [pa, sa, ta, qa]

rs = choice(l)

print(f"""
O aluno escolhido foi {rs}.
""")
