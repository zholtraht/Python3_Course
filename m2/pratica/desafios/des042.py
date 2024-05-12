ps = float(input("Primeiro segmento... "))
ss = float(input("Segundo segmento... "))
ts = float(input("Terceiro semento... "))

c1 = (ss + ts)
c2 = (ps + ts)
c3 = (ps + ss)

if ps < c1 and ss < c2 and ts < c3:
    print(f"""
Um triangulo foi formado:""")

    if ps == ss == ts:
        print("""
TRIANGULO EQUILATERO""")

    elif ps != ss != ts != ps:
        print("""
TRIANGULO ESCALENO""")
        
    else:
        print("""
TRIANGULO ISOCELES""")

else:
    print(
"""
Um triangulo NAO PODE ser formado.""")
