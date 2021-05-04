print("Digite la altura a la que se encuentra el objeto del suelo (m):")
h = int(input())
g = 9.81
t = (((2 * h) / g) ** 0.5)
print("El tiempo que se tardaría en llegar al suelo es de:",t,"seg")