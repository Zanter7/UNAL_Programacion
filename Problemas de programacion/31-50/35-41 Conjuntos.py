"""
OC: sean A1,A2 arreglos de numeros enteros, representando conjuntos
 Solucion a los ejercicios 35 - 41
"""
def union(A1,A2):
    array= A1+A2
    for i in array: # eliminacion de elementos repetidos
        while  array.count(i) > 1:
            array.remove(i)
    return array

def interseccion(A1,A2):
    array =[]
    for i in A1:
        if i in A2 and i not in array: #filtro elementos repetidos
            array.append(i)
    return array

def diferencia(A1,A2):
    if len(A2) == 0:
        return A1
    if A2[0] in A1:
        A1.remove(A2[0])
    A2.pop(0)
    return diferencia(A1,A2)

def diferencia_simetrica(A1,A2):
    array= A1+A2
    for i in array: # eliminacion de elementos repetidos
        while  array.count(i) > 1:
            array.remove(i)

    for i in A1:
        if i in A2:
            array.remove(i)

    return array

def pertenece(A1,A2):
    elemento = int(input("ingrese numero a analizar pertenencia: "))
    if elemento in A1 and elemento in A2:
        return f"el elemento {elemento} pertenece a ambos conjuntos"
    if elemento in A1:
        return f"el elemento {elemento} pertenece a el conjunto 1"
    if elemento in A2:
        return f"el elemento {elemento} pertenece a el conjunto 2"
    return f"el elemento {elemento} no pertenece a ningun conjunto"

def contenido(A1,A2):
    for i in A1:
        if i not in A2:
            return "A1 no esta contenido en A2"
    return "A1 esta contenido en A2"

def menu(CA1,CA2):
    while True:
        A1 = CA1.copy()
        A2 = CA2.copy()
        print("")
        print("Bienvenido al operador de conjuntos")
        print(" 1.union \n 2 interseccion \n 3.diferencia \n 4.diferencia simetrica")
        print(" 5.pertenece \n 6.contenido \n 7.salir")
        modo = int(input("digite el numero del modo: "))
        if modo == 1:
            print(union(A1,A2))
        elif modo == 2:
            print(interseccion(A1,A2))
        elif modo == 3:
            print(diferencia(A1,A2))
        elif modo == 4:
            print(diferencia_simetrica(A1,A2))
        elif modo == 5:
            print(pertenece(A1,A2))
        elif modo == 6:
            print(contenido(A1,A2))
        elif modo == 7:
            return "terminado" # salir del bucle while
        else:
            print("selector equivocado")


A = [int(c) for c in input('Ingrese arreglo: ').split(',')]
B = [int(c) for c in input('Ingrese arreglo 2: ').split(',')]

z = menu(A,B)

print(z)
