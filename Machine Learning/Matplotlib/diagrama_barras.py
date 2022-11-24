import matplotlib.pyplot as plt

x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [3, 9, 15, 20,0]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [5, 11, 17, 22,0]

plt.bar(x1, y1, label="Datos A", color="green", width=0.5)
plt.bar(x2, y2, label="Dates B", color="red", width=0.5)

plt.title("Economia Argentina")
plt.xlabel("Tiempo")
plt.ylabel("Inflacion")

plt.legend()
plt.show()