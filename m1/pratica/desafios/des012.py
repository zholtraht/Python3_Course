vp = float(input('Valor do produto... R$'))
vd = vp * 5 / 100
pd = vp - vd

print(f''''
Vejamos... O valor digitado e R${vp:.2f}
Esse produto com 5% de desconto vale R${pd:.2f}
''')
