"""
OC: constate de gravitacion, masa 1 y 2 y radio
    sea m1 la masa del objeto 1
    sea m2 la masa del objeto 2
    sea r la constante de gravitacion universal
relacion: formula g*m1*m2/r**2
    sea g la constante de gravitacion universal
    
OD: Fuerza
"""

def gravitacion(m1,m2,r):
    G= 6.67384e-11
    f = G*(m1*m2)/r**2
    return f

a=float(input("masa objeto 1: "))
b=float(input("masa objeto 2: "))
c=float(input("distancia R: "))

x=gravitacion(a,b,c)

print(f"la fuerza con la que se atraen los cuerpos es:\n {x} newtons")

#print(a,end='-') imprime "-" al final de lo impreso
#print(b, end='&') imprime "&" al final de lo impreso
#print(c)