import numpy as np

# Seleccionar un valor
matriz = np.array([(1,2,3,4),(5,6,7,8)])
print(matriz)

print("Fila 0, Columna 2: ", end="")
print(matriz[0,2])

print("Fila 0, Toda la columna 3: ", end="")
print(matriz[0:,3])

print("Menor valor de la matriz: ", end="")
print(matriz.min())

print("Mayor valor de la matriz: ", end="")
print(matriz.max())

print("Suma de los valores de la matriz: ", end="")
print(matriz.sum())

print("Desviacion estandar: ", end="")
print(np.std(matriz))

print("< - - - - - - - - - >")

x = np.array([(1,2,3),(4,5,6)])
y = np.array([(1,2,3),(4,5,6)])

print("Suma: ")
print(x+y)

print("Resta: ")
print(x-y)

print("Multiplicacion: ")
print(x*y)

print("Dvivision: ")
print(x/y)