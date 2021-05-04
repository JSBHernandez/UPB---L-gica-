def validar(email):
    caracter = "@"
    valido = False
    for v in email:
        if v == caracter:
            return True
    return False

correo = input("Ingrese su email: ")
if validar(correo):
    print("La dirección es válida")
else:
    print("La dirección es inválida")