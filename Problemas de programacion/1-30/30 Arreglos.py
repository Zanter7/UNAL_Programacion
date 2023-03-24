"""
OC: Sea array un arreglo de numeros enteros
OD: Sea array un arreglo de numeros enteros
R: Z_array = array desplazando 0 al final
"""

def zero_array(array):
    for i in range(len(array)-1):
        if array[i] == 0:
            array.pop(i)
            array.append(0)
    return array

a = [int(c) for c in input('Ingrese arreglo:').split(',')]

z = zero_array(a)

print(z)
