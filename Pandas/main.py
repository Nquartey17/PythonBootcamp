import pandas

data = pandas.read_csv("weather_data.csv")
# #Data frame - the entire table
# print(type(data))
# #Series - single column(s)
# print(type(data["temp"]))
#
# #Dictionary values for list
# data_dict = data.to_dict()
# print(data_dict)
#
# #Turn column into list
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# #Challenge - Calculate average of temperatures
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
#
# #Challenge 2 - Get max value using built in methods
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])
# print(data.condtion) # must match the column name exactly to use this (case sensitive)

#Get data in rows (Comment out code above to line 3 see this working)
print(data[data.day == "Monday"])

#Challenge 3 - Get row with highest temp of the week
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

#Challenge 4 - get Monday's temp and convert to Fahrenheit
fahrenheit = (monday.temp[0] * 9/5) + 32
print(fahrenheit)

#Create dataframe from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
data_2 = pandas.DataFrame(data_dict)
print(data_2)

#Turn dataframe to csv file
data_2.to_csv("new_data.csv")
