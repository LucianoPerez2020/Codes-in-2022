olympic_records = {
    "race":["50 butterfly", "50 back stroke", "50 breast stroke", "50 free"],
    "times":[22.27, 23.71, 24.95, 20.91],
    "year":[2018, 2022, 2022, 2009],
    "swimmer":["Andriy Govorov", "Kliment Kolesnikov", "Adam Peaty", "Cesar Cielo"]
    }

new_olympic_records = {
    "race":[],
    "times":[],
    "year":[],
    "swimmer":[]
}

new_olympic_records["gender"] = "M"
print(new_olympic_records)

new_olympic_records["gender"] = ""
print(new_olympic_records)

del new_olympic_records ["gender"]
print(new_olympic_records)

print(olympic_records['race'])
print(olympic_records.keys())
print(olympic_records.values())

edad = 18
if edad:
    print("mayor")
else:
    print("menor")

q = 1
status = False 
while status == False:
    q = q+1
    print(q)
    if (q >= 10):
        status = True