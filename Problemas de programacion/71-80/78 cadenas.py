"""
78. Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de ca-
racteres. El corrimiento circular a derecha de una cadena es poner el  ́ultimo car ́acter de la

cadena como primer car ́acter de la misma.
"""

def corrimiento_IZQ(txt):

    lista = list(txt) # convierte a lista
    caracter = lista[len(lista)-1] # cuarda el ultimo caracter
    lista.insert(0,caracter) # añade el caracter al inicio de la lista
    lista.pop() # elimina el ultimo caracter

    union = "".join(lista) #convierte a string
    return union

a = str(input("ingrese un string: "))

z = corrimiento_IZQ(a)

print(z)