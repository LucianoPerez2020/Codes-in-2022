import numpy as np
import sys # Variables del interprete
import time

# Matriz unidimensional
a = np.array([1,2,3])
print('1D array:')
print(a)

# Matriz bidimensional
b = np.array([(1,2,3), (4,5,6)])
print('2D array:')
print(b)

print("< - - - - - - - - - >")

# Demostracion de que Numpy usa menmos espacio que las propias listas de python.

P = range(1000)
print('Resultado lista de Python: ', end="")
print(sys.getsizeof(5) * len(P))

N = np.arange(1000)
print('Resultado NumPy array: ', end="")
print (N.size * N.itemsize)

print("< - - - - - - - - - >")

# Demostración de que Numpy es más rapido que python.

SIZE = 1000000
L1 = range (SIZE)
L2 = range (SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)
start = time.time()

result = [(x,y) for x,y in zip (L1, L2)]
print('Resultado lista de Python: ', end="")
print((time.time() - start) * 1000)

start = time.time()
result = A1+A2
print('Resultado NumPy array: ', end="")
print((time.time()-start)*1000)