"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95"""
menu = """
Bienvenido a la Universidad Centroamericana, por favor seleccione su carrera
[1] Derecho.
[2] Psicologia.
{3] Comunicacion.
[4] Ingenieria en Sistemas.
[5] Ingenieria Industrial.
"""
print(menu)

opcion = input("Digite la opcion que corresponda a su carrea: ")

if opcion =="1":
    print("Derecho")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    promedio = int(input("Ingrese su promedio: "))
    if promedio >= 85:
        print("El estudiantes es apto para la beca")
    else: 
        print("El estudiante no es apto para la beca")
elif opcion =="2": 
    print("Psicologia")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    promedio = int(input("Ingrese su promedio: "))
    if promedio >= 85:
        print("El estudiantes es apto para la beca")
    else: 
        print("El estudiante no es apto para la beca")
elif opcion =="3":
    print("Comunicacion")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    promedio = int(input("Ingrese su promedio: "))
    if promedio >= 85:
        print("El estudiantes es apto para la beca")
    else: 
        print("El estudiante no es apto para la beca")
elif opcion =="4":
    print("Ingenieria en Sistema")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    promedio = int(input("Ingrese su promedio: "))
    if promedio >= 95:
        print("El estudiantes es apto para la beca")
    else: 
        print("El estudiante no es apto para la beca")
elif opcion =="5":
    print("Ingenieria Industrial")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    promedio = int(input("Ingrese su promedio: "))
    if promedio >= 85:
        print("El estudiantes es apto para la beca")
    else: 
        print("El estudiante no es apto para la beca")
else:
	print ("")
	input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")