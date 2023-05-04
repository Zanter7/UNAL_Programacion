"""
71. Desarrollar un algoritmo que reciba como entrada un car ́acter y de como salida el n ́umero de
ocurrencias de dicho car ́acter en una cadena de caracteres.

OC: sea txt un string, sea caracter un ascii
OD: sea n un natural
R:  Para todo caracter en txt, s+=1
"""

def conta_caracter(txt,n):
    s=0
    txt.lower()
    for i in txt:
        if i == n:
            s+=1
    return s

a = str(input("ingrese una cadena de caracteres: "))
b = str(input("ingrese un caracter: "))

z = conta_caracter(a,b)

print(z)