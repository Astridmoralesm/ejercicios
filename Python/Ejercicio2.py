#Total a pagar por la compra de n cantida de productos

print("Ingrese la cantidad de productos a pagar:  ")
producto = int(input())
i = 0
total = 0
while i<producto:
    print("Producto ", i+1, "valor:  ")
    valor = int(input())
    print("Cantidad")
    cant = int(input())
    subtotal = valor * cant
    total = total+subtotal
    i+=1
    
print("El total es de: ", total)
