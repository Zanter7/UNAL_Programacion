"""
OC: sea r un numero entero radio de el circulo
OD: sea A el area del triangulo
R: A = 3 * sqrt(3)*r^2
"""
def area_triangulo(r):

    A = 3*(3**0.5)*r**2

    return A

a = int(input("radio del circulo: "))

z = area_triangulo(a)

print("el area del triangulo que circunscribe al circulo es: ",z)
