""""
OC: Sea A un arreglo de numeros reales
OD: Sea N un numero real
R: N la media del arreglo
"""


def bubblesort(array):
    n = 0  # Establecemos un contador del largo del vector
    for _ in array:
        n += 1
    for i in range(n-1):
        for j in range(0, n-i-1):
            # Revisa la matriz de 0 hasta n-i-1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def media(array):
    bubblesort(array)
    print(array)
    l = len(array)//2
    return array[l-1]


a = [int(c) for c in input('Ingrese arreglo:').split(',')]

z = media(a)

print(z)
