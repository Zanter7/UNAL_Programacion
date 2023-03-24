"""
OC: sea A un arreglo de numeros reales
OD: sea N un numero real
R: N = A[n]< A
"""
def minimo(A):
    if len(A) == 1:
        return A
    if A[0]< A[1]:
        A.pop(1)
    else:
        A.pop(0)
    return minimo(A)

a = [float(c) for c in input('Ingrese arreglo:').split(',')]

z = minimo(a)

print(z)
