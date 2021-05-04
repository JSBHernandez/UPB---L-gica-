def sumar(): #Definir la función sumar
    x = y + z
    print(("Resultado "),(x))
def resta(): #Definir la función restar
    x = y - z
    print(("Resultado "),(x))
def multiplicar(): #Definir la función multiplicar
    x = y * z
    print(("Resultado "),(x))
def dividir(): #Definir la función dividir
    x = y / z
    print(("Resultado "),(x))

while True:
    try: #Intentar obtener los datos de entrada
        y = int(input("Ingresa el primer número: \n"))
        z = int(input("Ingresa el segundo número: \n"))
        print(("¿Que cálculo desea realizar entre "), (y), ("y"), (z), ("?\n"))
        op = str(input("1- Sumar 2- Restar 3- Multiplicar 4- Dividir \n"))
    except: #Por si hay algún error
        print("Error")
        op = "?"

#Según la opción que se elija, se va a realizar determinada operación
    if op == "1":
        sumar()
        break
    elif op == "2":
        resta()
        break
    elif op == "3":
        multiplicar()
        break
    elif op == "4":
        dividir()
        break
    else: #En caso de que no se digite ningún dígito de la lista
        print("Ha ingresado un número que no está en la lista.")