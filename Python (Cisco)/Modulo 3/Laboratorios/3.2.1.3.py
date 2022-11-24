secret_number = 777

print("""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input("Ingrese su numero: "))

while number != secret_number:
    print("atrapadisimo por bot")
    number = int(input("Intenta de nuevo: "))
print("sos godin")