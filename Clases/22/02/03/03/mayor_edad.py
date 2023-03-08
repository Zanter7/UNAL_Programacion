def mayor_edad(edad):
    if edad >= 18:
        return "es mayor de edad"
    else:
        return "no es mayor de edad"

a = int(input("ingrese la edad: "))

z=mayor_edad(a)

print(z)
