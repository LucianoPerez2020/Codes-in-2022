# = es un operador de asignación, por ejemplo, a = b assigna a la varable a el valor de b.
# == es una pregunta ¿Son estos valores iguales? así que a == b compara a y b.

var = 0   # asignando 0 a var
print(var == 0)

var = 1  # asignando 1 a var
print(var == 0)

var = 0 # asignando 0 a var
print(var != 0)

var = 1 # asignando 1 a var
print(var != 0)

black_sheep > white_sheep  # mayor que
centigrade_outside >= 0.0  # mayor o igual que

current_velocity_mph < 85  # Menor que
current_velocity_mph <= 85  # Menor o igual que

#Instrucción condicional

# if the_weather_is_good: # Si el clima es bueno,
#    go_for_a_walk() #     saldremos a caminar
# else: #                   De lo contrario,
#    go_to_a_theater() #   iremos al cine.
# have_lunch() #            No importa si el clima es bueno o malo, almorzaremos después.

# No debes usar else sin un if precedente.
# else siempre es la última rama de la cascada, independientemente de si has usado elif o no.
# else es una parte opcional de la cascada, y puede omitirse.
# Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas.
# Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.

# WHILE

# Si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) poner sangría a todas las instrucciones de la misma manera.
# Una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del bucle.
# Si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, 
# el cuerpo no se ejecuta ni una sola vez (ten en cuenta la analogía de no tener que hacer nada si no hay nada que hacer).
# El cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al principio, el cuerpo podría funcionar continuamente hasta el infinito.

# FOR

# La palabra reservada for abre el bucle for; nota - No hay condición después de eso; 
# no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
# Cualquier variable después de la palabra reservada for es la variable de control del bucle; cuenta los giros del bucle y lo hace automáticamente.
# La palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.
# La función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; 
# en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99;0
# nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.
# Nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía : 
# la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto, if, elif, else y while expresan lo mismo).

# and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
# or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
# not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.