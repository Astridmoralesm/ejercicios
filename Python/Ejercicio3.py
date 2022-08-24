#Generar correo electronico

primernombre = input("Ingrese nombre: ")
segnombre = input("Ingrese su segundo nombre: ")
priapellido = input("Ingrese apellido: ")
segapellido = input("Ingrese su segundo apellido: ")

#usuarios.append((nombre,apellido))
 
mail = (primernombre.lower()[0]+priapellido.lower()+"@est.uca.edu.ni")
 
print("Su nuevo correo electronico es: ", mail)