import matplotlib.pyplot as plt

a = [1, 4, 8, 9, 15, 29, 35, 58,37, 14, 68, 78, 63, 83, 85]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(a, bins, histtype="bar", rwidth=1, color="green")

plt.title("Histograma")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()  