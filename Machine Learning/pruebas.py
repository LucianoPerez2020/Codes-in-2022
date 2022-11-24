import pandas as pd
DataFrame = pd.read_csv("tokyo_2020_swim.csv")

# print("Ganador: ")
# print(DataFrame.loc[1][3], end=" - ")
# print(DataFrame.loc[1][4], end=" - ")
# print(DataFrame.loc[1][6])

# print("Media de las columnas: ")
# Reaction_Time = DataFrame["reaction_time"]
# print(Reaction_Time.mean())

Team = DataFrame["team"]
ROC = 0
USA = 0
AUS = 0
FRA = 0
HUN = 0
ROU = 0
BRA = 0
ARG = 0

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

print(ROC)
print(USA)
print(AUS)
print(FRA)
print(HUN)
print(ROU)
print(BRA)
print(ARG)