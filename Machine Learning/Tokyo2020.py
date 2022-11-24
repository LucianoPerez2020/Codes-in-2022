import matplotlib.pyplot as plt
import pandas as pd
DataFrame = pd.read_csv("tokyo_2020_swim.csv")

#Definir los datos
Team = DataFrame["team"]
ROC = 0
USA = 0
AUS = 0
FRA = 0
HUN = 0
ROU = 0
BRA = 0
ARG = 0

# Contador de nadadores
for team in Team:
    match (team):
        case "ROC":
            ROC = ROC + 1
        case "USA":
            USA = USA + 1
        case "AUS":
            AUS = AUS + 1
        case "FRA":
            FRA = FRA + 1
        case "HUN":
            HUN = HUN + 1
        case "ROU":
            ROU = ROU + 1
        case "BRA":
            BRA = BRA + 1
        case "ARG":
            ARG = ARG + 1

# Muestra de grafico de torta
divisiones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
paises = ['ROC', 'USA', 'AUS', 'FRA', 'AUS', 'HUN', 'AUS', 'ROU', 'BRA', 'ARG' ]
colores = ['red', 'blue', '#FCBA2D', '#F28773', '#8b0000', 'green', 'yellow', 'gray', '#80ff00', '#40CFFF']

#Configurar las características del gráfico
plt.pie(divisiones, labels=paises, colors=colores, startangle=90, 
        shadow=False, explode=(0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01), autopct='%1.2f%%')

#Definir titulo
plt.title('Tokio 2020')
#Mostrar figura
plt.show()