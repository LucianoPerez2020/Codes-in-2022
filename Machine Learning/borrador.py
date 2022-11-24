import matplotlib.pyplot as plt
import pandas as pd
DataFrame = pd.read_csv("tokyo_2020_swim.csv")

#Definir los datos
Team = DataFrame["team"]
Reaction_Time = DataFrame["reaction_time"]
dq = DataFrame["dq"]
divisiones = [1, 20, 40]
actividades = ['Team', 'Reaction_Time', 'DQ']
colores = ['blue', 'red', 'grey'] 

#Configurar las características del gráfico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90, 
        shadow=False, explode=(0.01,0.01,0.01), autopct='%1.1f%%')

#Definir titulo
plt.title('Tokio 2020')
#Mostrar figura
plt.show()