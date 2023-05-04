def leer():

    cad = input("ingrese matriz separando filas por ; y columnas por , ")

    filas = cad.split(',')

    for i in range(len(filas)):
        filas[i] =  filas[i].split(',')
    for i in range(len(filas)):
        for j in range(len(filas[i])):
            filas[i][j] = float(filas[i][j])


def imprimir(A):
  for i in range(len(A)):
    print('|', end=' ')
    for j in range(len(A[i])):
      print(A[i][j], end=' ')
    print('|')


def multiplica(A,B):

    c = []
    n = len(A)
    m = len(A[0])
    l = len(B[0])

    for i in range(n):
        c.append([])
        for j in range(l):
            s=0
            for k in range(m):
                s+= A[i][k]*B[k][j]
            c[i].append(s)
    return imprimir(c)


a = [[3,4],[6,8],[2,1]]
b = [[2,6],[4,3]]

z = multiplica(a,b)

print(z)
