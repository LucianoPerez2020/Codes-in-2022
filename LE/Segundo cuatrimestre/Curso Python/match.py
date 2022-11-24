suma1 = int(input("Numero uno: "))
suma2 = int(input("Numero dos: "))
suma = suma1 + suma2
print(suma)

def resultado_de_suma(suma):
    match suma:
        case (2):
            print("Su numero es 2")
        case (3):
            print("Su numero es 3")