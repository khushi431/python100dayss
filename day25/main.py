import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns

# print(data["condition"])
# print(data.condition)


# get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# # monday_temp = int(ser.iloc[0])
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Tej"],
#     "scores": [76, 56, 89]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("squirrel_census.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")




