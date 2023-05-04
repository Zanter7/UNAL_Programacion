"""
54. Desarrollar un algoritmo que determine si una matriz es m ́agica. Se dice que una matriz
cuadrada es m ́agica si la suma de cada una de sus filas, de cada una de sus columnas y de
cada diagonal es igual.
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


######################


def suma_fila(M):
    a = 0
    b = 0
    for k in range(len(M[0])):
        a += M[0][k]
    for i in range(len(M)):
        b = 0
        for j in range(len(M[0])):
            b += M[i][j]
        
        if a != b:
            return False
    return True

def suma_columna(M):
    a = 0
    b = 0
    for k in range(len(M)):
        a += M[k][0]
    for i in range(len(M)):
        b = 0
        for j in range(len(M[0])):
            b += M[j][i]
        if a != b:
            return False
    return True

def diagonal(M):
    c = 0
    for i in range(len(M)):
        c += M[i][i]
#####
    d = 0
    for i in range(len(M)):
        d += M[i][len(M)-1-i]

    a = 0
    for k in range(len(M)):
        a += M[k][0]
    
    if a!= c or a!=d:
        return False
    return True

def magic(M):
    if suma_fila(M) is True and suma_columna(M) is True and diagonal(M) is True:
        return True
    return False


x = leer()
z = (magic(x))

print(z)