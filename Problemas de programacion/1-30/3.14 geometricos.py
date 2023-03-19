"""
OC: sea m1,m2 numeros reales
    sea b1,b2 numeros reales
    OD: sea tipo un string
R:  str = "perpendicular" si = m1 * m2 = -1
    str = "paralelo" si m1 = m2 y b1 != b2
    str = "ninguna" en otro caso

"""
def rectas(m1,m2,b1,b2):

    if m1 * m2 == -1:
        return "perpendicular"
    elif m1 == m2 and b1 != b2:
        return "paralelo"
    return "ninguna"

a = eval(input("recta 1 pendiente: "))
b = eval(input("recta 2 pendiente: "))
c = eval(input("recta 1 corte: "))
d = eval(input("recta 2 corte: "))

z = rectas(a,b,c,d)

print(z)
