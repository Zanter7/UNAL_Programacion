"""
OC: Sea n un numero natural
OD: Sea b un booleano
R: b = True si n es numero de fibonacci
   b = False en otro caso
    funcion secundaria esfiborec
    OC: Sean F1, F2, N naturales donde F1, F2 son numeros de fibonacci
    OD: Sea B un booleano
    R:  esfiborec(f2,f1+f2,n) si f1 + f2 < n
        B = True si f1+f2 = n
        B = False en otro caso

"""

def esfiborec(f1,f2,n):
    if f1+f2<n:
        return esfiborec(f2,f1+f2,n)
    else:
        return f1 + f2 == n

def esFibo (n):
    if n <= 1:
        return True
    else:
        return esfiborec(1,1,n)


a = int(input("Ingrese un numero: "))

z =esFibo(a)

print("el numero ",a, " pertenece a la sucesion de fibonacci?: ", z)