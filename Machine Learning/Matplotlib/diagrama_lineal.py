import matplotlib.pyplot as plt

# Definir datos
x1 = [0,-5, -10, 0]
y1 = [2, 5, 0, -5]
x2 = [0,5, 10, 0]
y2 = [2, 5, 0, -5]

# Caracteristicas del grafico
plt.plot(x1, y1, label="Vos", color="brown", linewidth=1)
plt.plot(x2, y2, label="Yo", color="yellow", linewidth=1)

# Titulo y nombres de eje
plt.title("Corazon para Mara")
plt.xlabel("Amarillo cono mi pelo")
plt.ylabel("Marron como tus ojos")

# Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()