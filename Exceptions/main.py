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