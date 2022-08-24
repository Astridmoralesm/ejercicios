#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.

precio = []
cantidad = int(input("Cantidad: "))
i = 1
mayor = 0
menor = 0
while(cantidad > 0):
    num = float(input("Precio # " + str(i) + ": "))
    precio.append(num)
    i = i + 1
    cantidad = cantidad - 1

mayor = max(precio)
menor = min(precio)

print("Precios: ", precio)
print("El precio mas alto es: ", mayor)
print("El precio mas bajo es: ", menor)