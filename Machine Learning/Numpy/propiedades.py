import numpy as np

# Matriz de 3 filas y 4 columnas con "unos"
print("Matriz de unos: ")
unos = np.ones((3,4))
print(unos)

# Matriz de 3 filas y 4 columnas con "ceros"
print("Matriz de ceros: ")
ceros = np.zeros((3,4))
print(ceros)

# Matriz de 3 filas y 3 columnas con numeros aleatorios
print("Matriz de aleatorios: ")
aleatorios = np.random.random((3,3))
print(aleatorios)

# Matriz vacia
print("Matriz vacia: ")
vacia = np.empty((3,3))
print(vacia)
# Porque tira numeros aleatorios???

# Tipo de dato
print("Tipo de dato: ", end="")
valor = np.array([(1, 2, 3)])
print(valor.dtype)

# Tamaño y forma de la matriz
print("Tamaño: ", end="")
valor3 = np.array([(1,2,3,4,5,6)])
print(valor3.size)
print("Forma: ", end="")
print(valor3.shape)

# Cambio de forma de una matriz
print("Original:")
forma = np.array([(8,9,10),(11,12,13)])
print(forma)
print("Modificado:")
forma = forma.reshape(3,2)
print(forma)