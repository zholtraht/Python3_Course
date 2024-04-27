#Crie um programa que:
#Leia a largura e a altura de uma parede em metros.
#Calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Considere que cada litro de tinta pinta uma área de 2 metros quadrados.

lp = float(input("Largura da parede... "))
ap = float(input("Altura da parede... "))
a = (lp * ap)
t = (a / 2)

print(f"""
Vejamos...

Sua parede possui dimensão {lp:.0f}x{ap:.0f}, e área {a:.1f}m².

Para pitar essa parede, precisas de {t:.1f}l de tinta.
""")
