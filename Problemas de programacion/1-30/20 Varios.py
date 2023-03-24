"""
OC: Sean k,i numeros enteros
OD: sea IS,IC numeros enteros
R: I_S = k*i*7
   I_C = k(1+i)**7
"""
def interes(k,i):

    t = ((i*100)/k)/100 # conversion de interes en pesos a taza porcentual y luego a decimal

    print(t)

    I_S =  k*t*7

    I_C = k*(1+ t)**7

    return f"con interes: simple {I_S} , compuesto {I_C} "

a = int(input("cantidad prestada: "))
b = int(input("interes en pesos: "))

z = interes(a,b)

print(z)
