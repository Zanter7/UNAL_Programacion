"""
74. Desarrollar un algoritmo que invierta una cadena de caracteres.
"""

def invertir(txt):

    return "".join(reversed(txt))

a = str(input("ingrese cadena a invertir: "))

z = invertir(a)

print(z)
