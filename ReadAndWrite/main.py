with open(file="/Users/15714/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

with open(file="../../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)


