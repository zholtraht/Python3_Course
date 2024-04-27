#Crie um programa que:
#Leia quanto dinheiro uma pessoa tem na carteira.
#Mostre quantos dólares ela pode comprar. 
#Cotação do dia: U$5.01

r = float(input("Quantidade de dinheiro na carteira... "))
d = r / 5.01

print(f"""
Vejamos...

Você possui R${r:.2f}.

Com essa quantia você pode comprar U${d:.2f}.
""")
