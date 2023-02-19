def L_leche(v, n, m, y, x):
    # v = cantidad de vacas
    # n = ancho de corral
    # m = largo de corral
    # y = M2 pasto por vaca para hacer producción
    # x = litros producibles

    at = n*m  # area total del corral
    p = at//v  # area para cada vaca

    # comprueba la cantidad de pasto disponible por vaca es < a la cantidad necesaria para dar leche
    if p < y:
        l = 'las vacas no tienen suficiente espacio para producir leche'
    else:
        # Calcula la cantidad de leche producida por las vacas
        t = v * x
        l = 'El total de leche es '+str(t)+' L'
    return l


a = int(input('cantidad de vacas: '))
b = int(input('ancho de corral: '))
c = int(input('largo de corral: '))
d = int(input('metros cuadrados de pasto para la produccion: '))
e = int(input('cantidad de litros que produce una vaca: '))

z = L_leche(a, b, c, d, e)

print(z)
