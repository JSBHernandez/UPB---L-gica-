def sumaDigitos(numero):
    sum = 0
    while numero != 0:
        dig = numero % 10
        sum = sum + dig
        numero = numero // 10
    return sum


num = int(input("Número a procesar: "))
while num != 0:
    print("Suma:", sumaDigitos(num))
    num = int(input("Número a procesar: "))