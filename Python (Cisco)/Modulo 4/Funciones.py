def message():
    print("Ingresa un valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "número")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    #Valor default

def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def address(street, city, postal_code):
    print("Tu dirección es:", street, city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")

address(s, c, p_c)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1).
# Paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2).
# Una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).

#Ejemplo 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # salida: 3
subtra(2, 5)    # salida: -3

#Ejemplo 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # salida: 3
subtra(b=2, a=5)    # salida: 3

#Ejemplo 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # salida: 3
subtra(5, 2)    # salida: 3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes: # Si wishes no es true se termina la funcion.
        return
    
    print("¡Feliz año nuevo!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def año_de_prueba(año):
    if año % 2 == 0:
        return True
    else:
        return False

test_data = [2000, 2001, 2002, 2003]
test_results = [True, False, True, False]

for i in range(len(test_data)):     # En el rango de los valores de "test_data".
	yr = test_data[i]				# "yr" es igual al valor del momento de "test_data".
	print(yr,"->",end=" ")			# Me printea el año seguido de un "->" con un argumento "end" de espacio vacio para no hacer un salto de linea.

	result = año_de_prueba(yr)		
	# "result" es igual a lo que de el return de la funcion "año_de_prueba" con el valor asigando 
	# de la variable "yr" que despues sera tomado en la misma funcion como el valor de "año".

	if result == test_results[i]:	# Si "result" tiene el mismo valor que el valor de "test_results[i]"...
		print("Bien")
	else:							# Si no...
		print("Mal")