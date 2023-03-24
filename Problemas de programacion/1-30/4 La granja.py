"""
OC: Sean P,Q,S,N,M numeros enteros donde
    P: Valor alambre de puas por metro
    Q: Valor tablas por metro
    S: Valor varillas por metro
    N: Largo de cerca
    M: Ancho de cerca
OD: Sea L un string
R: P,Q,S,N,M -> L
    L = "puas" si (2N+2M)*P*5 < (2N+2M)*Q*4 y (2N+2M)*P*5 < (2N+2M)*S*8
    L = "tabla" si (2N+2M)*Q*4 < (2N+2M)*P*5 y (2N+2M)*Q*4 < (2N+2M)*S*8
    L = "varilla" si (2N+2M)*S*8 < (2N+2M)*P*5 y (2N+2M)*S*8 < (2N+2M)*Q*4
"""

def Cercado(P,Q,S,N,M):
    #calcular perimetro de cerca con N+N+M+M
    per= 2*N+2*M

    #calcula cuanto vale cada cerramiento
    val_puas = per*P*5
    val_tabla = per*Q*4
    val_varilla = per*S*8

    if val_tabla < val_puas and val_tabla < val_varilla:
        l = "el cerramiento mas economico es de tablas por "+ str(val_tabla)
    elif val_puas < val_tabla and val_puas < val_varilla:
        l = "el cerramiento mas economico es de alambre de puas por "+ str(val_puas)
    elif val_varilla < val_tabla and val_varilla < val_puas:
        l = "el cerramiento mas economico es de varillas por "+ str(val_varilla)

    return l

a = int(input("Precio de alambre de puas por metro: "))
b = int(input("Precio de tabla por metro: "))
c = int(input("Precio de varilla por metro: "))

d = int(input("Ancho del corral: "))
e = int(input("Largo del corral: "))

z = Cercado(a,b,c,d,e)

print(z)
