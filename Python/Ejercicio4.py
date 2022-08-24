#Aplicar el IVA  a un producto 

precio = int(input("Ingrese el precio del producto: "))
IVA = 0.25
subtotal = precio * IVA
total = subtotal + precio
print("El total con IVA incluido es de: ", total)

