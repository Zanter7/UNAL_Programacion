"""
OC: Sea A (Aves) un numero natural
OD: Sea t un numero natural que represente el total de huevos en un mes
R: t = ((A//3)//2*30//5) + ((A//3)//2*30//3)
"""

def huevos(A):
    # teniendo en cuenta que no puede haber fraccion de gallina

    g = A//3
    m = g//2

    h_3dias = m * 30//3
    h_5dias = m * 30//5

    t = int(h_3dias + h_5dias)

    return t


a = int(input('total de aves en el galpon: '))

z = huevos(a)

print('el total de huevos producidos en un mes es: ', z)
