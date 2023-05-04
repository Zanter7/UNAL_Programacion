"""
55. Desarrollar un algoritmo que dado un entero, reemplace en una matriz todos los n ́umeros
mayores a un n ́umero dado por un uno y todos los menores o iguales por un cero.
"""

def leer():
    cad = input(
        'Ingrese matriz filas separadas por ; y columnas separadas  por ,\n')
    filas = cad.split(';')
    for i in range(len(filas)):
        filas[i] = filas[i].split(',')

    for i in range(len(filas)):
        for j in range(len(filas[i])):
            filas[i][j] = float(filas[i][j])
    return filas


def reemplazador(M,n):

    for i in range(len(M)):
        for j in range(len(M[0])):
            
            if M[i][j] > n :
                M[i][j] = 1
            else:
                M[i][j] = 0
    return M

matriz = leer()

num = int(input("numero para operar matriz: "))

z = reemplazador(matriz,num)

print(z)
