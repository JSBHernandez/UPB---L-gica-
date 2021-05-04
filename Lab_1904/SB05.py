def frecuencia(numero, dig):
    cant = 0
    while numero != 0:
        ultDigito = numero % 10
        if ultDigito == dig:
            cant += 1
        numero = numero // 10
    return cant

num = int(input("Número: "))
undigito = int(input("Dígito: "))
print("Frecuencia del dígito en el número:", frecuencia(num, undigito))