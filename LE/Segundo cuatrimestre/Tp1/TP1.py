olympic_record = {
    "race":"50 free",
    "time":20.91,
    "year":2009,
    "swimmer":"Cesar Cielo"
    }

new_olympic_record = {
    "race":"",
    "time":"",
    "year":"",
    "swimmer":""
}

update = "n"

new_olympic_record["race"] = input("Carrera: ")

new_olympic_record["time"] = float(input("Tiempo: "))
while olympic_record["time"] < new_olympic_record["time"]:
    print("El timepo ingresado es mayor que el record acutal.")
    new_olympic_record["time"] = int(input("Porfavor ingrese un timepo correcto: "))

new_olympic_record["year"] = int(input("Año: "))
while olympic_record["year"] > new_olympic_record["year"]:
    print("El año ingresado es anterior al actual.")
    new_olympic_record["year"] = int(input("Porfavor ingrese un año correcto: "))

new_olympic_record["swimmer"] = input("Nadador: ")
print("Felicidades por el record " + new_olympic_record["swimmer"] + " !!!")

update = input("Quiere reemplazar los nuevos datos por los antiguos?? y / n ")
if update == "y":
    for x in olympic_record:
        olympic_record[x] = new_olympic_record[x]
        
print(olympic_record)