import pandas as pd
import os

os.system("cls")
DataFrame = pd.read_csv("tokyo_2020_swim.csv")

print("Quinta columna: ", end="")
print(DataFrame[5])

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Quinta y decima columna: ", end="")
print(DataFrame[[5,10]])

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Primer valor de la fila en la quinta columna: ", end="")
print(DataFrame.iloc[0][2])

print("< - - - - - - - - - - - - - - - - - - - - - - >")

print("Valores de la primer fila: ", end="")
print(DataFrame.loc[0])