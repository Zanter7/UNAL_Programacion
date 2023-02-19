def divisible(x,y):
    """funcion que determine si un n ́umero es divisible por otro."""
    
    c = x%y #operador modulo, devuelve el residuo de la division

    if c == 0 :
        p=True
    else:
        p=False
    return p

a = int(input('ingrese dividendo: '))
b = int(input('ingrese divisor: '))

z = divisible(a,b)

if z is True:
    print(f" {a} es divisible por {b}")
else:
    print(f"{a} No es divisble por {b}")
