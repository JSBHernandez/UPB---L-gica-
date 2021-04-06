print("Digite la nota 1:")
n1 = int(input())
print("Digite la nota 2:")
n2 = int(input())
print("Digite la nota 3:")
n3 = int(input())
prom = ((n1 + n2 + n3) / 3)
if prom >= 7:
    print("Promocionado")
elif prom >= 4 and prom < 7:
    print("Regular")
else:
    print("Reprobado")
    