"""
OC: Sea A un arreglo de numeros reales
OD: sea S un numero real
Relacion: recursiva A[0]+sumarreglo(A)
"""


S = 0
def sumarreglo(A):
    if len(A) == 0:
        return 0
    return A.pop(0)+sumarreglo(A)


a = [float(c) for c in input('Ingrese arreglo:').split(',')]

z = sumarreglo(a)

print(z)
