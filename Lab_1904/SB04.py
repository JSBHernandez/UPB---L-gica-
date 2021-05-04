def primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

numero = int(input("Digite su número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")