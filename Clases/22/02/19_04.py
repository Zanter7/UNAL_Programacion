def leerVector():
    cad = input('Ingrese vector elementos separados  por ,')
    x = cad.split(',')
    for i in range(len(x)):
        x[i] = float(x[i])
    return x


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


def imprimir(A):
    for i in range(len(A)):
        print('|', end=' ')
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print('|')

# para toda fila i de A se toma cada columna j de B y el
# elemento Ci,j de la matriz resultante es la suma de
# la multiplicacion de dicha fila por dicha columna
# An*m Bm*l entonces Cn*l


def multiplica(A, B):
    C = []
    n = len(A)
    m = len(A[0])
    l = len(B[0])
    for i in range(n):
        C.append([])
        for j in range(l):
            s = 0
            for k in range(m):
                s += A[i][k]*B[k][j]
            C[i].append(s)
    return C


def crea_Gauss(A, b):
    C = []
    n = len(A)
    # Pega matriz A
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j])
    # Pega vector b
    for i in range(n):
        C[i].append(b[i])
    # Pega identidad
    for i in range(n):
        for j in range(n):
            C[i].append(1 if i == j else 0)
    return C


def reduce_fila(A, i):
    p = A[i][i]
    m = len(A[0])
    for j in range(m):
        A[i][j] /= p
    return A, p


def elimina(A, i, k):
    if i == k:
        return A
    m = len(A[0])
    v = -A[k][i]
    for j in range(m):
        A[k][j] += v*A[i][j]
    return A


def elimina_filas(A, i):
    n = len(A)
    for k in range(n):
        A = elimina(A, i, k)
    return A


def Gauss(A, b):
    C = crea_Gauss(A, b)
    n = len(C)
    d = 1
    for i in range(n):
        C, p = reduce_fila(C, i)
        C = elimina_filas(C, i)
        d *= p
    return C, d


# Programa principal
A = leer()
imprimir(A)

# 2 3 4   4
# 1 5 6   5
# 7 8 9   -1

b = leerVector()

print('============')
C, d = Gauss(A, b)
imprimir(C)
print('Determinante:', d)
# B = leer()
# imprimir(B)

# print('============')
# C = multiplica(A,B)
# imprimir(C)
