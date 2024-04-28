#Crie um programa que:
#Faça o computador “pensar” em um número inteiro entre 0 e 5.
#Peça para o usuário tentar descobrir qual foi o número escolhido.
#Escrever na tela se o usuário venceu ou perdeu.

from random import randint

n = randint(0, 5)

print("""
Acabo de pensar em um número inteiro entre 0 e 5.
{'=' * 10}
Tente adivinhar o número escolhido:
""")

ne = int(input("Seu palpite... "))

if ne == n:
    print("ACERTOU!! Acabas de me vencer.")
else:
    print(f"ERROU!! Minha escolha foi {n}.")
