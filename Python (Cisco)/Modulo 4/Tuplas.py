# Las listas son mutalbes
Lista = [1, 2, 3]

# Las tuplas son inmutables
Tupla = (1, 2, 3)

# end="->"
Diccionario = {
    "Luciano" : 18,
    "Mara" : 15,
    "Año" : 2022,
    "Mundial" : 24}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

dictionary = {
            "gato" : "chat",
            "perro" : "chien",
            "caballo" : "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

# Salida:
# gato -> chat
# león no está en el diccionario
# caballo -> cheval

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Ordena las salida de las palabras
for key in sorted(dictionary.keys()):

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

diccionario = {
#           "spanish" : "french",
            "gato" : "chat",
            "perro" : "chien",
            "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

dictionary = {'gato': 'minou', 'perro': 'chien', 'caballo': 'cheval'}

# Para cambiar el valor
dictionary['gato'] = 'minouuu'

# Para sumar un valor
dictionary['gato2'] = 'miau2'

# Para eliminar un valor
del dictionary['perro']

print(dictionary)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# NOTAS DE ESTUDIANTES
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }

item_1 = pol_esp_dictionary["gleba"]    # Ejemplo 1.
print(item_1)    # salida: tierra

item_2 = pol_esp_dictionary.get("woda")    # Ejemplo 2.
print(item_2)    # salida: agua