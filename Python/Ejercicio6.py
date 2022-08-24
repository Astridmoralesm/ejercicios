#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números enteros.

inicio = int(input("Ingrese el primer valor: ")) 
final = int(input("Ingrese un valor final: ")) 
  
for num in range(inicio, final + 1): 
    if num % 2 == 0: 
        print(num, end = " ") 