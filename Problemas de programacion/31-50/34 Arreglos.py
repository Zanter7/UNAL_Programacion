"""
OC: Sea "array" un arreglo de numeros enteros
OD: Sea N un numero entero
R: N = MCM array[0]...array[n]
"""
def MCD(a,b): # MCD de dos numeros
    if b == 0:
        return a
    
    return a*b / MCD(b,a%b)

def mcd_multiple(array):
    resultado = array[0]
    for i in range(len(array)):
        resultado = MCD(resultado,array[i])
    return resultado

A = [int(c) for c in input('Ingrese arreglo: ').split(',')]

z = mcd_multiple(A)

print(z)