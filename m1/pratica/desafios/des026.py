#Crie um programa que:
#Leia uma frase pelo teclado.
#Mostre quantas vezes aparece a letra “A”.
#Mostre em que posição a letra 'A' aparece a primeira vez.
#Mostre em que posição a letra 'A' aparece a última vez.

f = str(input("Uma frase... ")).strip().lower()

print(f"""
Vejamos... "{f.title()}"

A letra A aparece {f.count('a')} vezes na frase.
{'=' * 5}
A primeira letra A apareceu na posição {f.find('a')+1}.
{'=' * 5}
A última letra A apareceu na posição {f.rfind('a')+1}.
""")
