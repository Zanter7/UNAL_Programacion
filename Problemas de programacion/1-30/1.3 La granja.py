"""
OC: Sea E un numero natural que representa la cantidad de escorpiones
OD: Sea t un numero natural que representa Kg de escorpion
R: t = E//3 * (20+30+50)//3 (un tercio de los escorpiones por el promedio de peso)
"""

def Escorpiones(E):

    max_venta = E//3

    prom_peso = (20+30+50)//3

    t = max_venta*prom_peso

    return t


a = int(input('la cantidad de escorpiones es: '))

z = Escorpiones(a)

print('el peso maximo de escorpiones es: ', z, 'g')
