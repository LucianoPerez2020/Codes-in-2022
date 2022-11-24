numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

numbers = [111, 7, 2, 1]
print(numbers[-1]) # Ultimo
print(numbers[-2]) # Anteultimo

# Salida:
# 1
# 2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

# Salida:
# 4
# [111, 7, 2, 1]
# 5
# [111, 7, 2, 1, 4]
# 6
# [222, 111, 7, 2, 1, 4]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)
    print(my_list)

print(my_list)

# Salida:
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i
print(total)

# Salida:
# 27

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# Nota:
# Hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto).
# Hemos preparado el bucle for para que se ejecute su cuerpo length // 2 veces (esto funciona bien para listas con longitudes pares e impares,
# porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto).
# Hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length-i-1)
# (desde el final de la lista); en nuestro ejemplo, for i igual a 0 a la (length-i-1) da 4; for i igual a 3, da 3: esto es exactamente lo que necesitábamos.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # salida: [4, 2, 1, 3, 5]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Copiando la lista entera.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Elimina el contenido de la lista
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# Elimina la lista
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

squares = [x ** 2 for x in range(10)]
# Salida:  (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

twos = [2 ** i for i in range(8)]
# Salida:  (1, 2, 4, 8, 16, 32, 64, 128)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EMPTY = "-"
peon = "PEON"
torre = "TORRE"
caballo = "CABALLO"
tablero = []

for i in range(8):
    torre = [vacio for i in range(8)]
    tablero.append(torre)

tablero[0][0] = torre
tablero[0][7] = torre
tablero[7][0] = torre
tablero[7][7] = torre

print(tablero)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

temperaturas = [[0.0 for horas in range(24)] for dias in range(31)]
total = 0.0

for dia in temperaturas:
    total += dia[11]
promedio = total / 31

t_alta = -100.0
for dia in temperaturas:
    for temperatura in dia:
        if temperatura > t_alta:
            t_alta = temperatura

dias_calientes = 0
for dia in temperaturas:
    if dia[11] > 20.0:
        dias_calientes += 1

print("Temperatura promedio al mediodía: ",promedio)
print("La temperatura más alta fue: ",t_alta)
print("Días calurosos: ",dias_calientes)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Arreglos tridimencionales no pienso ver || 3.7.1.5 Listas en aplicaciones avanzadas Arreglos