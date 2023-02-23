def primo(n):
    p = 1 # variable que contendra divisiones de n/n hasta n/1
    d = 1  # variable que contendra divisiones de n//n hasta n//1
    e = n # variable que operara n/e y n//e desde e=n hasta e=1
    contador = 1 #cantidad de numeros por los que n es divisble

    for i in range(n-1):
        #comprueba si el numero es divisible entre todos sus anteriores
        p = n/e
        d = n//e

        if p == d:
            contador = contador + 1
        e = e-1
        if contador > 2:
            # si el numero tiene mas de dos divisores no es primo
            return f"el numero {n} NO es primo"
        
    return f"el numero {n} es primo"
    
a = int(input("ingrese un numero:"))

x = primo(a)

print(x)
