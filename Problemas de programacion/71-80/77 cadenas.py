"""
77. Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
caracteres. El corrimiento circular a izquierda es pasar el primer car ́acter de una cadena como
 ́ultimo car ́acter de la misma.
"""

def corrimiento_DER(txt):

    lista = list(txt) #convierte a lista

    lista.append(lista[0]) #añade el primer elemento al final
    lista.pop(0) #elimina el primer elemento

    union = "".join(lista) #convierte a string
    return union

a = str(input("ingrese un string: "))

z = corrimiento_DER(a)

print(z)
