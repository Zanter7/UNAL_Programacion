def leer_coeficiente(txt):
    if txt == "" or txt=="+":
        return 1.0
    if txt =="-":
        return -1.0
    return float(txt)

def leer_monomio(txt):
    s= txt.split("x")
    a = leer_coeficiente(s[0])
    if(len(s) == 1):
        b = 0
    elif s[1]=="0":
        b=1
    else: 
        b = int(s[1][1:len(s[1])])
    return a,b

def leer_polinomio1 (txt):
    i = 1
    while i<len(txt) and txt[i]!="+" and txt[i]!="-":
        i+=1
    if i == len(txt):
        return [leer_monomio(txt)]
    a = leer_polinomio1(txt[i:len(txt)])
    a.append(leer_monomio(txt[0:i]))
    return a

def max_grado(a):
    m = a[0][1]
    for i in range(1,len(a)):
        if a[i][1]>m:
            m = a[i][1]
    return m

def leer_polinomio(txt):
    a = leer_polinomio1(txt)
    n = max_grado(a)
    p = [0 for i in range (n+1)]

    for i in range(len(a)):
        p =[a[i][1]] = a[i][0]
    return p

ojo = input("polinomio: ")

z = leer_polinomio(ojo)

print(z)