"""
OC:sea a,b,c,x un numero natural donde
    a,b,c son coeficientes
    x es la variable
OD: sea derivada un numero natural
R: derivada = f'(ax^2+bx+c) = 2ax+b+0
"""
def derivada(a,b,c,x):

    c = 0

    deriv = 2*a*x+b+c

    return deriv

print ("de la forma (ax^2+bx+c) ingrese:")
w = int(input("ingrese coeficiente 1: "))
w2 = int(input("ingrese coeficiente 2: "))
y = int(input("ingrese termino independiente: "))
z = int(input("ingrese valor de la variable: "))

d = derivada(w,w2,y,z)

print(d)
