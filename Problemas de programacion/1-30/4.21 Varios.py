"""
OC: Sea n un numero natural, el tamaño de la base
OD: Sea f un numero entero, total de forma de organizar las fichas
R: F = n si n <= a 2
   F = formas(n-1) + formas (n-2)
"""

def forma (n):
    if n<= 2:
        return n
    else:
        return forma(n-1)+forma(n-2) #recursion

a = int(input("largo de ficha"))

z= forma(a)

print(z)
