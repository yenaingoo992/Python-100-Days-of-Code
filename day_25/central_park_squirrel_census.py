import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250201.csv")
colors = ["Gray", "Cinnamon", "Black"]
squirrel_count = {"Fur Color": colors, "count": []}
for color in colors:
    count = len(data[data["Primary Fur Color"] == f"{color}"])
    squirrel_count["count"].append(count)

pandas.DataFrame(squirrel_count).to_csv("squirrel_count.csv")