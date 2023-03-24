"""
OC: sean p,k,t numeros naturales
OD: sea A un numero natural
R: A = t//P*K
"""
def arboles(p,k,t):

    A = t//(p*k)

    return A

a = int(input("cantidad de hojas por rama: "))
b = int(input("cantidad de ramas que se quitaron por arbol: "))
c = int(input("hojas a obtener: "))

z = arboles(a,b,c)

print(f"la cantidad de arboles a podar es {z}")