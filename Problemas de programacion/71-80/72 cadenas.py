"""
72. Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es
subcadena de la segunda.
"""


def subcadena(txt1, txt2):
    
    if txt1 in txt2:
        return True
    return False


a = str(input("ingrese un string1: "))
b = str(input("ingrese un string a buscar dentro de string1: "))

z = subcadena(b, a)

print(z)
