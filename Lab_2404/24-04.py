datos = [4,5,9,10]
for i in range(0, 4):
    print(datos[i], end=" ")
print()
datos[2]=-10
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
datos.insert(1, 11)
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
datos.remove(5)
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
datos = datos + [21, 22]
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
