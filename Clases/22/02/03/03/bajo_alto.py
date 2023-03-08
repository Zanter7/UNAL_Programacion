"""
Objetos conocidos: sea h altura
Objeto desconocido: sea t "es alto" o "es medio" o "es bajo"
Relacion: natural -> ASCII*
h -> si h>=160 "es alto", si h>120 "es medio", el resto es "es bajo"
"""

def altura(h):

    if h >= 160:
        return "es alto"
    if h > 120:
        return "es medio"
    return "es bajo"


a = int(input("ingrese la altura: "))

z = altura(a)

print(z)
