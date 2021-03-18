print("Digite la Nota 1 (15%): ")
n1 = float(input())
if n1 > 5 or n1 < 0:
    print("La nota debe ser entre 0 a 5, intentelo de nuevo.")
    while n1 >= 6 or n1 < 0:
        print("Digite la Nota 1 (15%): ")
        n1 = float(input())
print("Digite la Nota 2 (15%): ")
n2 = float(input())
if n2 > 5 or n2 < 0:
    print("La nota debe ser entre 0 a 5, intentelo de nuevo.")
    while n2 >= 6 or n2 < 0:
        print("Digite la Nota 2 (15%): ")
        n2 = float(input())
print("Digite la Nota 3 (20%): ")
n3 = float(input())
if n3 > 5 or n3 < 0:
    print("La nota debe ser entre 0 a 5, intentelo de nuevo.")
    while n3 >= 6 or n3 < 0:
        print("Digite la Nota 3 (20%): ")
        n3 = float(input())
print("Digite la Nota 4 (20%): ")
n4 = float(input())
if n4 > 5 or n4 < 0:
    print("La nota debe ser entre 0 a 5, intentelo de nuevo.")
    while n4 >= 6 or n4 < 0:
        print("Digite la Nota 4 (20%): ")
        n4 = float(input())
print("Digite la Nota 5 (30%): ")
n5 = float(input())
if n5 > 5 or n5 < 0:
    print("La nota debe ser entre 0 a 5, intentelo de nuevo.")
    while n5 >= 6 or n5 <- 0:
        print("Digite la Nota 5 (30%): ")
        n5 = float(input())
# Calcular Notas
defin = ((n1 * 0.15) + (n2 * 0.15) + (n3 * 0.2) + (n4 * 0.2) + (n5 * 0.3))
print("Su nota definitiva es de: ", defin)
if defin >= 3:
    print("Aprobó la asignatura.")
else:
    print("Reprobó la asignatura")

