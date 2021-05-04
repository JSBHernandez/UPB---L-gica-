def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def frecuencia(numero, dig):
    cantidad = 0
    while numero != 0:
        ultDigito = numero % 10
        if ultDigito == dig:
            cantidad += 1
        numero = numero // 10
    return cantidad

def factorial(numero):
    f = 1
    if numero != 0:
        for i in range(1, numero + 1):
            f = f * i
    return f

def sumaDigitos(numero):
    sum = 0
    while numero != 0:
        dig = numero % 10
        sum = sum + dig
        numero = numero // 10
    return sum

mayor = 0
numero = int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:", sumaDigitos(numero))
    dig = int(input("Dígito: "))
    print("El", dig, "aparece", frecuencia(numero, dig), "veces")
    if numero > mayor:
        mayor = numero
    numero = int(input("Número primo: "))
print("Factorial de", mayor, ":", factorial(mayor))