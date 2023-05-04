"""
53. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
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


def suma_fila(M, N):
    a = 0
    for i in range(len(M[0])):
        a += M[N][i]
    return a


z = leer()
x = int(input("ingrese una fila cosiderando el 0"))

w = suma_fila(z, x)

print(w)
