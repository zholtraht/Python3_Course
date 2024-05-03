vc = float(input("Valor da casa... "))
sc = float(input("Salario do comprador... "))
af = int(input("Anos de financiamento... "))

vp = vc / (af * 12)

if vp > (sc * 30) / 100:
    print("""
NEGADO!!

O valor da prestação mensal excedeu 30% de seu salario.
O empréstimo nao pode ser aprovado...
""")
    
else:
    print("""
APROVADO!!
          
O valor da prestação mensal esta dentro de sua margem salarial.
O empréstimo pode ser aprovado...
""")
