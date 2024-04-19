from random import shuffle

pa = str(input('Primeiro aluno...'))
sa = str(input('Segudo aluno...'))
ta = str(input('Terceiro aluno...'))
qa = str(input('Quarto aluno...'))
l = [pa, sa, ta, qa]
rs = shuffle(l)

print(f'''
A ordem de apresentacao sera: {l}
''')
