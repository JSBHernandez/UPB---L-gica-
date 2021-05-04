def sumaDigitos(num):
    sum = 0
    while num != 0:
        digito = num % 10
        sum = sum + digito
        num = num // 10
    return sum

cantidad = 0
mayor = -1
num = int(input("Número positivo: "))
while num >= 0:
    sum = sumaDigitos(num)
    if sum > mayor:
        mayor = sum
        n_mayorsuma = num
    if sum < 10:
        cantidad += 1
    num = int(input("Número positivo: "))
print("Sumatoria de dígitos de", n_mayorsuma, ":", mayor)
print("Cantidad con sumatoria menor a 10:", cantidad)