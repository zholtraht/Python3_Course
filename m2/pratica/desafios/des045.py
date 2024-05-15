from random import randint

print(
f"""
[ 1 ] PEDRA.
[ 2 ] PAPEL.
[ 3 ] TESOURA.
""")

ej = int(input("Sua jogada... (1, 2, 3) "))
ec = randint(1, 3)

if ej == ec:
    print("""
EMPATE""")

elif ej == 1 and ec == 3:
    print("""
GANHOU""")

elif ej == 1 and ec == 2:
    print("""
PERDEU""")

elif ej == 2 and ec == 1:
    print("""
GANHOU""")

elif ej == 2 and ec == 3:
    print("""
PERDEU""")

elif ej == 3 and ec == 2:
    print("""
GANHOU""")

elif ej == 3 and ec == 1:
    print("""
PERDEU""")
