"""
OC: sea m1,m2 numeros reales
    sea b1,b2 numeros reales
OD: sean R1_Cx,R1_Cy,R2_Cx,R2_Cy" un real
R:  R1_Cx = m1(0)+b1
    R1_Cy = -b1/m1
    R2_Cx = m2(0)+b2
    R2_Cy = -b2/m2

"""
def rectas(m1,m2,b1,b2):

    R1_Cy = m1*0+b1
    R1_Cx = (-b1)/m1
    R2_Cy = m2*0+b2
    R2_Cx = (-b2)/m2

    U = f"recta 1 corte: X {R1_Cx} y {R1_Cy} \n recta 2 corte : x {R2_Cx} y {R2_Cy}"

    return U


a = eval(input("recta 1 pendiente: "))
b = eval(input("recta 2 pendiente: "))
c = eval(input("recta 1 corte: "))
d = eval(input("recta 2 corte: "))

z = rectas(a,b,c,d)

print(z)
