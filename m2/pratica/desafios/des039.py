from datetime import date

print(
f"""
{'=' * 16}
[ m ] masculino.
[ f ] feminino.
{'=' * 16}
""")

s = str(input(
"""
Qual o seu sexo? (m / f) """)).lower()

if s == 'f':
    print(
"""
O serviso obrigatorio de alistamento, so e atribuido a cidadoes do sexo masculino.
""")

quit()
    
da = date.today().year
an = int(input("Ano de nascimento... "))
i = (da - an)

if i == 18:
    print(
f"""
Deve se alistar imediatamente.
{'=' * 30}

Voce tem {i} anos.
Devera se apresentar ainda esse ano {da}.
""")

elif i < 18:
    print(
f"""
Devera ainda se alistar.
{'=' * 24}

Voce tem {i} anos.
Devera se apresentar em {an + 18}. Ainda te faltam {18 - i} ano(s).
""")

else:
    print(
f"""
Deveria ter se alistado.
{'=' * 24}

Voce tem {i} anos.
Devera se apresentar imediatamente e pagar a multa. Seu ano de aistamento foi em {an + 18}
""")
