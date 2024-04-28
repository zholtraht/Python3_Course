#Crie um programa que:
#Leia o nome de uma cidade.
#Diga se ela começa ou não com o nome “SANTO”.

c = str(input("Em que cidade você nasceu?... ")).strip()

print(c[0:5].upper() == 'SANTO')
