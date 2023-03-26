"""
OC: sea "array" un arreglo de numeros enteros
OD: sea MCD un entero
R: MCD = minimo comun divisor entre A[0],A[1]...A[n]
"""
def MCD(a,b): # MCD de dos numeros
    if b == 0:
        return a
    return MCD(b,a%b)

def mcd_multiple(array):
    resultado = array[0]
    for i in range(len(array)):
        resultado = MCD(resultado,array[i])
    return resultado

A = [int(c) for c in input('Ingrese arreglo: ').split(',')]

z = mcd_multiple(A)

print(z)
