# Comparador de identidad (is)
# El operador ìs se utiliza para comparar la identidad de dos objetos. 
# Esto es, si los objetos a los que las variables hacen referencia son el mismo o no. 
# Lo indica que esta comparación es más estricta que la realizada por el operador ==.

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except:
    print('No se que hacer con', value)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Cuando usamos expext ponemos el nombre del error que nos podria saltar como si fuera que asi se llama,
# en caso de especificar ninguno "except" sera el default que abarcara a todos ahi.

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Esto es lo mismo que antes
temperature = float(input('Ingresa la temperatura actual:'))

if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    print("Por debajo de cero")
else:
    print("Cero")