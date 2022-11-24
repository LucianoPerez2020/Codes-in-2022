import matplotlib.pyplot as plt

x1 = [0.25, 1.25, 2.25, 3.25]
y1 = [3, 9, 15, 20]
x2 = [0.75, 1.75, 2.75, 3.75]
y2 = [50, 68, 99, 48]

plt.scatter(x1, y1, label="Datos A", color="green")
plt.scatter(x2, y2, label="Dates B", color="red")

plt.title("Dispersion")
plt.xlabel("Tiempo")
plt.ylabel("Inflacion")

plt.legend()
plt.show()