# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("anidado: x == 6")
    elif x == 10:  # True
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Bucle infinito
while True:
    print("Estoy atrapado dentro de un bucle.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

i = 0
while i < 100:
    # do_something()
    i += 1

# es lo mismo que 

for i in range(100):
    # do_something()
    pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# break - ejemplo
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# continue - ejemplo
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")