#Crie um programa que:
#Leia o preço de um produto.
#Mostre seu novo preço, com 5% de desconto.

vp = float(input("Valor do produto... R$"))
vd = (vp * 5 / 100)
pd = (vp - vd)

print(f"""
Vejamos...
O valor digitado é R${vp:.2f}.
Esse produto com 5% de desconto vale R${pd:.2f}.
""")
