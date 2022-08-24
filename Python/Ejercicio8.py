#Leer x cantidad de edades y mostrar el promedio de dichas edades.

promedio = 0
n = int (input("Ingresa el valor de x: "))
for i in range (1, n + 1):
    edad = int (input("Ingresa la edad: "))
    promedio=promedio+edad
    print ()
if n == 0:
    promedio = 0
else:
    promedio=promedio/n

print ("Promedio de edades: " + repr (promedio))