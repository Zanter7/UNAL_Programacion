"""
76. Desarrollar un algoritmo que determina si una cadena de caracteres es frase pal ́ındrome. Una
cadena se dice frase pal ́ındrome si la cadena al eliminarle los espacios es pal ́ındrome.
"""

def frase_palindromo(txt):

    union = list(txt) # covnertir a arreglo
    while " " in union: # eliminar espacios 
        union.remove(" ")
    union = "".join(union) # convertir a string

    inverso = "".join(reversed(union))

    if inverso == union:
        return True
    return False

a = str(input("ingrese una cadena para saber si la frase es palindroma: "))

z = frase_palindromo(a)

print(z)
