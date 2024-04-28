#Crie um programa que:
#Leia a velocidade de um carro.
#Ultrapassando 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#Considere que a multa vai custar R$7,00 por cada Km acima do limite.

vc = float(input("Velocidade do carro... "))
vm = (vc - 80) * 7

if vc > 80:
    print(f"""
    MULTADO!!!

    Você estava a {vc - 80}km acima da velocidade permitida.

    Será multado em R${vm:.2f}
    """)

else:
    print("""
    EM ORDEM...

    Conduza com cuidado!!
    """)
