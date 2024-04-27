#Crie um programa que:
#Leia um número Inteiro.
#Mostre na tela a sua tabuada.

n = int(input("Um número... "))

print(f"""
TABUADA DE {n}:

{'=' * 13}
{n} x 1  = {n * 1} 
{n} x 2  = {n * 2}
{n} x 3  = {n * 3}
{n} x 4  = {n * 4}
{n} x 5  = {n * 5}
{n} x 6  = {n * 6}
{n} x 7  = {n * 7}
{n} x 8  = {n * 8}
{n} x 9  = {n * 9}
{n} x 10 = {n * 10}
{'=' * 13}
""")
