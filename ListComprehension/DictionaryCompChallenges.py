#Challenge 1: Get length of each word in sentence as put in dictionary
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()
result = {word:len(word) for word in sentence}
print(result)

#Challenge 2: Convert temperatures in Celsius to Fahrenheit in dictionary
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}
print(weather_f)