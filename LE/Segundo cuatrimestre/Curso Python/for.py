# La variable iteradora me recorre la coleccion elemento por elemento, por lo tanto, la 
# cantidad de elementos que halla va a ser la cantidad de veces que se repita el bucle.

# for i (variable iteradora) in [1, 2, 3, 4, 5] (elemento):
for i in [1, 20, 3, 41, 5, "Seis"]:
    print(i, end="_ ")
    print("Programacion ATS.")

# Esto es lo mismo que antes pero escirto de una mejor manera.

lista = [1, 20, 3, 41, 5, "Seis"]
for i in lista:
    print(i, end="_ ")
    print("Programacion ATS.")

print("- - - - -")

diccionario = {
    "Faker":"active",
    "Rekkles":"inactive",
    "Josedeodo":"active"
}

# Aca solo me va a mostrar las palabras claves.
for i in diccionario:
    print(i)

# Y aca las claves con sus valores.
for clave,valor in diccionario.items():
    print(f"Jugaodr: {clave}, estado: {valor}")

# O solo los valores.
for clave,valor in diccionario.items():
    print(f"Estado: {valor}")

print("- - - - -")

for i in "Python":
    print(i, end="-")