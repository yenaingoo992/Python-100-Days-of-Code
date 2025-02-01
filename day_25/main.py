# with open("./weather_data.csv") as file:
#     contents = file.readlines()
#     for line in contents:
#         print(line.strip())

# import csv
# with open("./weather_data.csv") as file:
#     csv_data = csv.reader(file)
#     temperature = []
#     for row in csv_data:
#         if row[1] != "temperature":
#             temperature.append(row[1])
#     print(temperature)

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data)
print(data["temperature"])
print(type(data)) # DataFrame, means 2 dimensional
print(type(data["temperature"])) # Series, means 1 dimensional for each column

temperature_as_list = data["temperature"].tolist()

# to find average
average_temperature = sum(temperature_as_list)/len(temperature_as_list)
print(average_temperature)

# with pandas
print(data["temperature"].mean())
print(data.temperature.max())

# to read row
print(data[data.day == "Monday"])

# finding max temperature day
print(data[data.temperature == data.temperature.max()])

# getting single data from Series
monday = data[data.day == "Monday"]
temperature_in_fahrenheit = monday.temperature[0] * 9 / 5 + 32
print(temperature_in_fahrenheit)

# create dataframe from dict
data_dict = {
    "students": ["Amy", "James", "Leon"],
    "scores": [56, 45, 63]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("student.csv")