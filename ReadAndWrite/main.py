# with open(file="my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Remember to close files if you're not using with because python might close it when more resources are needed

# Modes: w - write, a - add
with open(file="new_file.txt", mode="a") as file:
    file.write("\nNew text.")

# If you try to write to a file that doesn't exist, it will be created
