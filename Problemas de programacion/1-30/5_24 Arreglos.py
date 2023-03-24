"""
OC: sea A un arreglo de numeros reales
OD: sea P un real
R: A = A[0] + A // len(A)
"""


def sumarreglo(A):
    S = 0
    for i in range(len(A)):
        S += A[i]
        print(S)
    S = S/len(A)
    return S


a = [float(c) for c in input('Ingrese arreglo:').split(',')]

z = sumarreglo(a)

print(z)
