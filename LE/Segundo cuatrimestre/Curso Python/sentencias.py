#Porque tengo que especificar qie tipo de variable es??
q = int(input("Ingrese su numero: "))
if q == 0:
    print("Su numero es 0")
elif q >= 1:
    print("Su numero es positivo")
else:
    print("Su numero es negativo")

uno, dos = 1, 2
cien = 0
while cien <= 100:
    print(cien)
    cien = cien + uno + dos