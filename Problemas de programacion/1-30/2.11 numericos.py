"""
OC: sea a,b un numero natural donde
    a son coeficientes
OD: sea resultado un numero natural
Relacion: resultado = f'(ax^2+bx+c) = 2ax+b+0 (coef lineal de derivada) = 2a
(segun las reglas de derivacion el exponente multiplica a el coeficiente y hace-1,
por lo que da un solo numero acompañando la variable ya que en la segunda parte hace x^(1-1))
"""
def coef_derivada(a):

    coef = 2*a

    return coef

coefi = int(input("ingrese 'a' de (ax^2+bx+c): "))

z = coef_derivada(coefi)

print(z)
