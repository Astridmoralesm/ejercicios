"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro.
"""

total=1000
print("Bienvenido al banco LAFISE\n\
¿Qué desea realizar?!\n\
1.- Ingresar dinero:\n\
2.- Sacar dinero:\n\
3.-Salir:\n")
opcion=int(input())
if opcion==1:
    ingreso=float(input("¿Cuanto dinero deseas ingresar?:"))
    total+=ingreso
    print("Tu saldo es de" , total)
elif opcion==2:
    egreso=float(input("¿Cuanto dinero desea retirar?:"))
    if total-egreso<0:
        print("Lo sentimos, no puede retirar esa cantidad debido a que su saldo solo es de", total)
    else:
        total-=egreso
        print("Tu saldo es de ", total)
elif opcion==3:
    quit()