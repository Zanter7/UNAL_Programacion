def potencia(N, E):
    """potencia de un entero elevado a un entero"""

    p = 1

    if E == 0:
        p = 1

    else:
        for i in range(E):
            p = p*N
    return p


a = int(input("numero entero base: "))
b = int(input("exponente: "))

z = potencia(a, b)

print('el total es: ',z)
