def factorial(num):
    f = 1
    if num != 0:
        for x in range(1, num + 1):
            f = f * x
    return f

cantidad = 0
n = int(input("Número (-1 para cortar): "))
while n != -1:
    print("Factorial:", factorial(n))
    cantidad += 1
    n = int(input("Número (-1 para cortar): "))
print("Se leyeron", cantidad, "números")