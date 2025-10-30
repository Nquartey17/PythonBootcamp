try: #input code that could create exception
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError: #Specify exception type
    file = open("a_file.txt", "w")
    file.write("test")
except KeyError as error_message:
    print(f"{error_message} key does not exist")
else: #when no errors are found
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


#Exception raising
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldn't be over 3 meters")

bmi = weight / height ** 2
print(bmi)