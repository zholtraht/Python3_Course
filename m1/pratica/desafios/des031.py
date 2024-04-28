#Crie um programa que:
#pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem.
#Cobre R$0,50 por Km para viagens de até 200Km.
#Cobre R$0,45 parta viagens mais longas.

km = float(input("Valor em quilometros... "))
v1 = (km * 0.50)
v2 = (km * 0.45)

if km > 200:
    print(f"""
    R${v2:.2f}
    """)
else:
    print(f"""
    R${v1:.2f}
    """)
