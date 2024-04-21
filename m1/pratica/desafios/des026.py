f = str(input('Digite uma frase...')).strip().lower()

print(f'''
Vejamos... "{f.title()}"
A letra A aparece {f.count('a')} vezes na frase.
A primeira letra A apareceu na posicao {f.find('a')+1}.
A ultima letra A apareceu na posicao {f.rfind('a')+1}.
''')
