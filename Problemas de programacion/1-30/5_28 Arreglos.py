"""
OC: Sean A,B arreglos de numeros reales
OD: Sea "Punta" un arreglo de numeros reales
R: Punta = [A[0]*B[0],A[1]*B[1],A[2]*B[2]...A[n]*B[n]]
"""
def producto_directo(A,B):
    if len(A) == 0 or len(B) == 0:
        return []
    return [A[0]*B[0]]+producto_directo(A[1:],B[1:]) #rebando desde el elemento 1 hasta el n element

a = [float(c) for c in input('Ingrese arreglo:').split(',')]
b = [float(c) for c in input('Ingrese arreglo 2 :').split(',')]

z = producto_directo(a,b)

print(z)
