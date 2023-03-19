"""
OC: sean n1,n2, multiplo numeros enteros
OD: booleano
Relacion: n1 + n2 -> multilpo
"""
def multiplo_suma(n1,n2,multiplo):
    k = n1 + n2
    if multiplo % k == 0:
        return True
    return False

a = int(input('ingrese numero 1: '))
b = int(input('ingrese numero 2: '))
c = int(input('ingrese multiplo: '))

z = multiplo_suma(a,b,c)

print(f'{c} es multiplo de {a+b}:', z)
