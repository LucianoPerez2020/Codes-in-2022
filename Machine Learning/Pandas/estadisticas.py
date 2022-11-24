import pandas as pd
import os

# guardar la salida en un bloc de notas

os.system("cls")
DataFrame = pd.read_csv("tokyo_2020_swim.csv")
print("DataFrame: ")
print(DataFrame)

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Filas x Columnas: ", end="")
print(DataFrame.shape)

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Total de filas: ", end="")
print(len(DataFrame.index))

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Estadisticas del DataFrame: ")
print(DataFrame.describe())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Media de las columnas: ")
print(DataFrame.mean())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Correlacion: ")
print(DataFrame.corr())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Valor mas alto por columna: ")
print(DataFrame.max())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Valor mas bajo por columna: ")
print(DataFrame.min())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Valor medio por columna: ")
print(DataFrame.median())