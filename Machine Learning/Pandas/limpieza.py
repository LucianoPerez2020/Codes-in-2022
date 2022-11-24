import pandas as pd
import os

os.system("cls")
DataFrame = pd.read_csv("tokyo_2020_swim.csv")

print("True = faltantes || False = no perdidos: ")
print(DataFrame.isnull())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Eliminamos filas con valores perdidos: ")
print(DataFrame.dropna())

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Eliminamos columnas con valores perdidos: ")
print(DataFrame.dropna(axis = 1))

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Reemplaza los valores perdidos con 0: ")
print(DataFrame.fillna(0))