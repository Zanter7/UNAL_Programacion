def potencia(N,E):
    p=1
    for i in range(E):
        p=p*N
    return p

a = int(input("numero entero base: "))
b = int(input("exponente: "))

z =potencia(a,b)

print(z)
