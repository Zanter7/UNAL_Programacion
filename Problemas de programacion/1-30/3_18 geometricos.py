"""
OC: sea r un entero, radio de telaraña
OD: sea a un entero
R: a = 6*r+(3*r*(r+1)) como operacion reducida
"""


def telarana(r):
    return 6*r+(3*r*(r+1))

a = int(input("tamaño de la telaraña: "))

z= telarana(a)

print("la telaraña usa: ", z, "cm de telaraña")
