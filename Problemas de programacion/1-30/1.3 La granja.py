def Escorpiones(E):

    max_venta = E//3

    prom_peso = (20+30+50)//3

    t = max_venta*prom_peso

    return t


a = int(input('la cantidad de escorpiones es: '))

z = Escorpiones(a)

print('el peso maximo de escorpiones es: ', z, 'g')
