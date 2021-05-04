a = int(input("¿Cuantos nombres de personas quieres ingresar? "))
b = []
c = []
x=0
y=0
for i in range (0,a):
 b.append(input("Ingresa el nombre de una persona a la que quieras agregrar a la lista: "))
print ("Estos son todos los nombres:",b)
for j in range (0,a):
 c.append(len(b[j]))
 print("El nombre",b[x],"tiene",c[y],"letras")
 x=x+1
 y=y+1