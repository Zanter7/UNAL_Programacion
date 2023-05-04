"""
Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera est ́a
incluida en la segunda. Se dice que una cadena est ́a incluida en otra, si todos los caracteres
(con repeticiones) de la cadena est ́a en la segunda cadena sin tener en cuenta el orden de los
caracteres.
"""


def incluida(txt1, txt2):

    for i in range(len(txt1)):
        if txt1[i] not in txt2:
            return False
    return True


a = str(input("ingrese la cadena 1: "))
b = str(input("ingrese la cadena 2: "))

z = incluida(a,b)

print(z)
