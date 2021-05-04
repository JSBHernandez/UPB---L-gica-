tam = int(input("Ingrese la cantidad de valores que quiere ver:"))
mult = int(input("Ingrese el número para ver sus múltiplos:"))
mults = []
for num in range(1,tam+1):
 mults.append(num*mult)
print("Los multiplos de",mult,"son:",mults)