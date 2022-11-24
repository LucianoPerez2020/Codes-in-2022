# Idea: servidor en el que los juegadores inactivos sean eliminados.

# uso un diccionario (el cual puede ser mutado)
servidor = {
    "Faker":"active",
    "Josedeodo":"active",
    "Caps":"inactive",
    "Rekkles":"active",
    "Lucho_ssj":"inactive"
}

for usuario, estado in servidor.copy().items():
    if estado == "inactive":
        del servidor[usuario]

servidor_active = {}

for usuario, estado in servidor.items():
    if estado == "active":
        servidor_active[usuario] = estado

print(servidor)