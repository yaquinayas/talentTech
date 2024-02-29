

def devolverdistintos(x, y, z):
    lista = [x, y, z]
    list.sort(lista)
    if x + y + z > 15:
        
        return lista[2]
    elif x + y + z < 10:
        return lista[0]
    else:
        return lista[1]

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))
print("La suma es: ", x + y + z)
print("DevolverDistintos: ", devolverdistintos(x, y, z))