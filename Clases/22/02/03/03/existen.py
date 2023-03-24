def existe(A,x):
    S= False
    for i in range(len(A)):
        S = S or A[i]==x
    return S

a = [int(c) for c in input('Ingrese arreglo:').split(',')]
b = int(input("ingrese el numero entero a buscar: "))

z = existe(a,b)

print (z)
