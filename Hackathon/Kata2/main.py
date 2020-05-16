password = "contraseña"
password_ususario = input("Introduzca la contraseña: ")

password_ususario = password_ususario.lower()
if(password == password_ususario):
    print("El password es correcto")
else:
    print("El password es incorrecto")    