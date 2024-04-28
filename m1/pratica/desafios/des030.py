#Crie um programa que:
#Leia um número inteiro.
#Mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("Digite um número... "))
m = n % 2 

if m == 0:
    print("""
    PAR
    """)
else:
    print("""
    IMPAR
    """)
