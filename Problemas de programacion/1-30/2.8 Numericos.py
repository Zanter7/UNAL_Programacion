def primos_relativos(a, b):
    div_1 = 1
    div_2 = 1
    e = a
    g = b
    contador = 0

    for i in range(a-1):

        div_1 = a % e
        div_2 = b % g

        if div_1 == div_2:
            contador += 1
        e -= 1
        g -= 1
        if contador > 2:
            return f"no primos relativos {contador}"
    return f"SON primos relativos {contador}"

c=int(input("ingrese un numero: "))
d=int(input("ingrese otro numero: "))

z=primos_relativos(c,d)

print(z)
print(10/100)
