print(
f"""
{'=' * 5} GpuraByte {'=' * 5}
""")

pc = float(input("Preco das compras... "))

print(
"""
FORMAS DE PAGAMENTO

[ 1 ] a vista (dinheiro / cheque).
[ 2 ] a vista (cartao).
[ 3 ] 2x (cartao).
[ 4 ] 3x (cartao).
""")

op = int(input("Qual a opcao? (1, 2, 3, 4) "))

if op == 1:
    cp = pc - (pc * 10 / 100) 

    print(
f"""
Valor da compra: R${pc:.2f}.

Condicao de pagamento: R${cp:.2f}.
""")

elif op == 2:
    cp = pc - (pc * 5 / 100)

    print(
f"""
Valor da compra: R${pc:.2f}.

Condicao de pagamento: R${cp:.2f}.
""")

elif op == 3:
    print(
f"""
Valor da compra: R${pc:.2f}.

Condicao de pagamento: R${pc:.2f}.
""")

elif op == 4:
    qp = int(input("Quantas parcelas? "))
    cp = pc + (pc * 20 / 100)

    print(
f"""
Valor da compra: R${pc:.2f}.

Condicao de pagamento: R${cp:.2f}.
""")

else:
    print(
"""
Essa nao e uma opcao disponivel
""")
