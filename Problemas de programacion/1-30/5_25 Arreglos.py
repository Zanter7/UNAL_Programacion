"""
OC: Sea A,B un arreglo de numeros reales
OD: Sea P un arreglo de numeros reales
R: P = (A[1]*B[1]...A[n]*B[n])
"""
def Producto_punto(A,B):
    if len(A) == 0 or len(B) == 0:
        return 0
    return A.pop(0)*B.pop(0)+ Producto_punto(A,B)

a = [float(c) for c in input('Ingrese arreglo:').split(',')]
b = [float(c) for c in input('Ingrese arreglo 2 :').split(',')]

z = Producto_punto(a,b)

print(z)
