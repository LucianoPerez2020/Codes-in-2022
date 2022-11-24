#   +---+---+---+---+---+---+
#   | P | y | t | h | o | n |
#   +---+---+---+---+---+---+
#   0   1   2   3   4   5   6
#   -6  -5  -4  -3  -2  -1

numeros_primos = [2, 3, 5, 7]
print(numeros_primos)

print(numeros_primos[0])
print(numeros_primos + [1, 4, 6])

numeros_primos [0] = 100
print(numeros_primos)

letras = ["a", "b", "c", "d", "e"]
print(letras[0:2])
print(letras[3:])

letras[0:3] = ["A", "B", "C"]
print(letras)

letras[0] = 1, 2, 3
print(letras)

del letras[4]
print(letras)

word = "Todas iguales"
print(word[1])
print(word[1+1])
print(word[-1])
print(word[2:])
print(word[:2])

usarname = "Luciano"
adress = "Perez"
print(usarname + adress)