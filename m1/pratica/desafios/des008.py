m = float(input('Digite um valor em metros...'))
dam = m / 10
hm = m / 100
km = m / 1000
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'''
A medida de {m}m corresponde a {dm}dm, {cm}cm, {mm}mm, {dam}dam, {hm}hm, e {km}km
''')
