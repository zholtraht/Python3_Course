#Crie um programa que:
#Pergunte a quantidade de Km percorridos por um carro alugado.
#Perunte a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar.
#Considere que o carro custa R$60 por dia e R$0,15 por Km rodado.

qd = int(input("""Dias alugados?... """))
qk = float(input("""Km's rodados?... """))
v = qd * 60 + qk * 0.15

print(f"""
vejamos...

Você alugou por {qd} dias.
rodou {qk:.1f}km.

O total a pagar é R${v:.2f}.
""")
