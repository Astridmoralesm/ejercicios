#Leer dos números y decir cual es mayor y cual es menor.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 >= num2:
    print("El mayor es ",num1)
if num2 >= num1:
    print("El mayor es ", num2)
if num1 <= num2:
    print("El menor es ",num1)
if num2 <= num1:
    print("El menor es ", num2)
