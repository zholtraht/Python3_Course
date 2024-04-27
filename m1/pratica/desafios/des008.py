#Crie um programa que:
#Leia um valor em metros.
#Exiba o valor convertido em centímetros e milímetros.

m = float(input("Valor em metros... "))
dam = m / 10
hm = m / 100
km = m / 1000
dm = m * 10
cm = m * 100
mm = m * 1000

print(f"""
A medida de {m}m corresponde a:

{dm}dm.
{'=' * 5}
{cm}cm.
{'=' * 5}
{mm}mm.
{'=' * 5}
{dam}dam.
{'=' * 5}
{hm}hm.
{'=' * 5}
{km}km.
""")
