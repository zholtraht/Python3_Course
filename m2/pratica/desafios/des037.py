n = int(input("Um numero... "))

print(
f"""
{'=' * 12}
[ 1 ] BINARIO.
[ 2 ] OCTAL.
[ 3 ] HEXADECIMAL.
{'=' * 12}
""")

escolha = int(input("Qual sera a base de conversao? (1, 2, 3) "))


if escolha == 1:
    print(
f"""
{n} convertido para binario e igual a {bin(n)[2:]}.
""")
    
elif escolha == 2:
    print(
f"""
{n} convertido para octal e igual a {oct(n)[2:]}.
""")

elif escolha == 3:
    print(
f"""
{n} convertido para hexadecimal e igual a {hex(n)[2:]}.
""")

else:
    print(
f"""
Essa nao e uma das opcoes disponiveis.
tente novamente e escolha entre as opcoes "1, 2, e 3"
""")
