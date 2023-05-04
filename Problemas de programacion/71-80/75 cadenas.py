"""
75. Desarrollar un algoritmo que determine si una cadena de caracteres es pal ́ındrome. Una cadena
se dice pal ́indrome si al invertirla es igual a ella misma.
"""

def palindromo(txt):
    inverso = "".join(reversed(txt))
    if inverso == txt:
        return True
    return False

a = str(input("ingrese una cadena para saber si es palindroma: "))

z = palindromo(a)

print(z)
