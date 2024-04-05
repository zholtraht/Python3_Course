v = input('Digite algo...')

print(f'''
Vejamos...voce digitou {v}.
     
Tipo primitivo: {type(v)}
Es numerico?: {v.isnumeric()}
Es alfabetico?: {v.isalpha()}
Es alfanumerico?: {v.isalnum()}
Es somente espacos?: {v.isspace()}
Es somente maiusculas?: {v.isupper()}
Es somente minusculas?: {v.islower()}
Es capitalizado?: {v.istitle()}
''')
