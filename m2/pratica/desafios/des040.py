n1 = float(input("Primeira nota... "))
n2 = float(input("Segunda nota... "))

m = (n1 + n2) / 2

if m >= 7:
    print(
f"""
APROVADO!!

Voce obteve media {m:.1f}.
""")
    
elif m >= 5 and m < 7:
    print(
f"""
RECUPERACAO!!

Voce obteve media {m:.1f}.
""")

else:
    print(
f"""
REPROVADO!!

Voce obteve media {m:.1f}.
""")
