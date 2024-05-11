from datetime import date

aa = date.today().year
an = int(input("Ano de nascimento... "))
i = (aa - an)

if i <= 9:
    print(
f"""
Voce possui {i} anos.

Voce e um atleta MIRIM.
""")

elif i > 9 and i <= 14:
    print(
f"""
Voce possui {i} anos.

Voce e um atleta INFANTIL.
""")

elif i > 14 and i <= 19:
    print(
f"""
Voce possui {i} anos.

Voce e um atleta JUNIOR.
""")
    
elif i > 19 and i <= 25:
    print(
f"""
Voce possui {i} anos.

Voce e um atleta SENIOR.
""")

else:
    print(
f"""
Voce possui {i} anos.

Voce e um atleta MASTER.
""")
