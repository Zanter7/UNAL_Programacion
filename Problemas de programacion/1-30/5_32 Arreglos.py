"""
OC: Sea N un numero natural
OD: Sea "array" un arreglo
R: array = N convertido a base 2 e invertido
"""

#def binario(N):
#    B=[]
#    while N > 0:
# #        B.append(N%2)
#        N//=2
#    return(B)

def binario(N):
    N=[N]
    if N[0] == 0:
        return []
    return [N[0]%2] + binario(N[0]//2)


a = int(input("ingrese numero: "))

z = binario(a)

print(z)
