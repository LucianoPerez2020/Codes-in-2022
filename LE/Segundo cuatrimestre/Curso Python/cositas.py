high = 100
low = 20 - 10
high_low = high + low
print(high_low)

# Mutable: se puede eliminar, agregar datos.
# Inmutable: no se pueden modificar los datos.

# Mutable, con corchetes.
lista = []

# Inmutable, con parentesis.
tupla = ()

# Mutable, con llaves.
diccionario = {
    "Clave1":"Valor1",
    "Clave2":["Valor1", "Valor2"]
}

#[5, 6, 7, 8, 9]
list_1 = 0
list_1 = list(range(5, 10))
print(list_1)

#[0, 3, 6, 9]
list_2 = 0
list_2 = list(range(0, 10, 3))
print(list_2)

#[-10, -40, -70]
list_3 = 0
list_3 = list(range(-10, -100, -30))
print(list_3)