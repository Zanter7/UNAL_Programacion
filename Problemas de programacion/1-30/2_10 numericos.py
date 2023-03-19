"""
OC: sea a,b,c,n un numero natural donde
    a,b,c son coeficientes
    n es variable
OD: sea resultado un numero natural
Relacion: "resultado" = a(n)^2+b(n)+c
"""
def ev_polinomio(a,b,c,n):

    resultado = a*(n**2)+b*n+c

    return resultado

w = int(input("ingrese coeficiente 1: "))
x = int(input("ingrese coeficiente 2: "))
y = int(input("ingrese termino independiente: "))
z = int(input("ingrese valor de la variable: "))

v = ev_polinomio(w,x,y,z)

print(v)
