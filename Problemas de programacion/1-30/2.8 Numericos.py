"""
OC: sean a,b numeros enteros
OD: sea t un string
R: t = "No son primos relativos" si MCD(a,b)>1
   t = "primos relativo" en otro caso
"""

def primos_relativos(a, b):
    div_1 = 1
    div_2 = 1
    e = a

    contador = 0

    for i in range(a):

        div_1 = a % e
        div_2 = b % e

        if div_1 == 0 and div_2 == 0:
            contador += 1
        e -= 1

        if contador >= 2:
            return "no primos relativos"
    return "SON primos relativos"

c=int(input("ingrese un numero: "))
d=int(input("ingrese otro numero: "))

z=primos_relativos(c,d)

print(z)

