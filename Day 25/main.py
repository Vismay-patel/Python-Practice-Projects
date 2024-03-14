# import csv

# with open("Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))

# print(temperature)


import pandas as pd

# data = pd.read_csv("Day 25/weather_data.csv")

# data_dict = data.to_dict()

# # print(data_dict)

# temp_list = data["temp"].to_list()

# # print(f"Average Temperature: {round(sum(temp_list)/len(temp_list))}")

# # print(data["temp"].max())j

# # print(data[data['day'] == 'Mondayj'])

# # print(data[data['temp'] == data['temp'].max()])

# monday = data[data['day'] == "Monday"]

# print(monday['temp'] [0  ])

data = pd.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = len(data[data['Primary Fur Color'] == "Black"])
cinnamon = len(data[data['Primary Fur Color'] == "Cinnamon"])
gray = len(data[data['Primary Fur Color'] == "Gray"])

print(black)
print(cinnamon)
print(gray)

data_dict = {
    "Fur Color": ["black", "cinnamon", "gray"],
    "Count": [black, cinnamon , gray]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("Day 25/new_csv_file.csv")