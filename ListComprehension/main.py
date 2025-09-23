numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1

new_list.append(add_1)
print(new_list)

#list comprehension: "list name" = ["function" for "element" in "list"]
lc_list = [n+1 for n in numbers]
print(lc_list)

name = "Niikwartei"
letter_list = [n for n in name]
print(letter_list)

range_list = [n * 2 for n in range(1,5)]
print(range_list)

#Conditional list comprehension: "list name" = ["function" for "element" in "list" if "test is T/F"]
multiple_names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

#Challenge: Get list of names with length <= 4
short_names = [name for name in multiple_names if len(name) <= 4]
print(short_names)

#Challenge: get longer names and make them all uppercase
long_names =[name.upper() for name in multiple_names if len(name) >= 5]
print(long_names)
