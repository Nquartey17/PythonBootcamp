# List comprehension of numbers squared
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Convert nums to string, then get list of all even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers_2 = [int(num) for num in list_of_strings]
result = [num for num in numbers_2 if num % 2 == 0]
print(result)

