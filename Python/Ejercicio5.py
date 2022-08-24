#Calcular edad

nombre = input("Ingrese su nombre: ")
anoactual = int(input("Ingresa el valor del año actual: "))
anonacimiento = int(input("Ingresa el valor del año de nacimiento: "))
dia_actual = int (input("Ingresa el valor del dia actual: "))
dia_nacimiento = int(input ('Ingresa el valor del dia de nacimiento: '))
mes_actual = int (input("Ingresa el valor del mes actual: "))
mes_nacimiento = int(input("Ingresa el valor del mes de nacimiento: "))
edad=anoactual-anonacimiento
if mes_nacimiento>mes_actual or (mes_nacimiento==mes_actual and dia_nacimiento>dia_actual):
    edad=edad-1
print (nombre, "tiene " + repr (edad), " años. ")
