#Crie um programa que:
#Leia uma temperatura em graus Celsius.
#Converta para graus Fahrenheit.

c = float(input("Informe um valor em ⁰C... "))
f = (c * 9/5) + 32

print(f"""
Você digitou {c:.1f}⁰C.
Essa temperatura convertida em fahrenheit é {f:.1f}⁰F.
""")
