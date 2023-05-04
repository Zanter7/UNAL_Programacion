"""
52. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
"""

def leer():
    cad = input(
        'Ingrese matriz filas separadas por ; y columnas separadas  por ,')
    filas = cad.split(';')
    for i in range(len(filas)):
        filas[i] = filas[i].split(',')

    for i in range(len(filas)):
        for j in range(len(filas[i])):
            filas[i][j] = float(filas[i][j])
    return filas


def suma_columna(M, N):
    a = 0
    for i in range(len(M)):
        a += M[i][N]
    return a


z = leer()
x = int(input("ingrese una columna cosiderando el 0"))

w = suma_columna(z, x)

print(w)
