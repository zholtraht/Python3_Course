#Crie um programa que:
#Leia o nome de uma pessoa.
#Diga se ela tem “SILVA” no nome.

n = str(input("Seu nome... ")).strip().lower().title()

print(f"""
Seu nome tem 'Silva'? {'Silva' in n}
""")
