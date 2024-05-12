p = float(input("Seu peso... "))
a = float(input("Sua altura... "))
imc = p / (a ** 2)

print(
f"""
Seu IMC e de {imc:.1f}.""")

if imc < 18.5:
    print(
"""
Esta ABAIXO DO PESO.
""")
    
elif imc >= 18.5 and imc < 25:
    print(
"""
Esta no PESO IDEAL.
""")
    
elif imc >= 25 and imc < 30:
    print(
"""
Esta no SOBREPESO.
""")
    
elif imc >= 30 and imc < 40:
    print(
"""
Esta na OBESIDADE.
""")
    
else:
    print(
"""
Esta na OBESIDADE MORBIDA.
""")
