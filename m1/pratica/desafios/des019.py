from random import choice

pa = str(input('Primeiro aluno...'))
sa = str(input('Segundo aluno...'))
ta = str(input('Terceiro aluno...'))
qa = str(input('Quarto aluno...'))
l = [pa, sa, ta, qa]
rs = choice(l)

print(f'''
O aluno escolhido foi {rs}
''')
