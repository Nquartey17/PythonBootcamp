import pandas

# Challenge - Get count of different fur color and turn into csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250729.csv")

data_dict = {
    "Fur color": ["Gray","Cinnamon","Black"],
    "Count": [len(data[data['Primary Fur Color'] == "Gray"]), len(data[data['Primary Fur Color'] == "Cinnamon"]), len(data[data['Primary Fur Color'] == "Black"])]
}

data_2 = pandas.DataFrame(data_dict)
data_2.to_csv("squirrel_count.csv")