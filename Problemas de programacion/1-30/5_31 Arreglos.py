"""
OC: Sea array un arreglo en base 2
OD: Sea N un entero
R: N = array invertido convertido a base 10
"""
def binario_invert(array):
    for i in range(len(array)):
        array.insert(0, array.pop(i))
    return array

def decimal(A):
    if len(A) == 0:
        return 0
    return A.pop(0)*(2**(len(A)))+decimal(A)

a = [int(c) for c in input('Ingrese arreglo: ').split(',')]

z = decimal(binario_invert(a))

print(z)
