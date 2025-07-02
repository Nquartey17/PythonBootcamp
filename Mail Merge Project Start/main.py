
#for each name in invited_names.txt
with open(file="Input/Names/invited_names.txt") as file1:
    contents = file1.readlines()
    for i in range(len(contents)):
        print(contents[i])

with open(file="./Input/Letters/starting_letter.txt") as file2:
    txt = file2.read()
    print(txt)
    for name in contents:
        stripped_name = name.strip()
        new_letter = txt.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as file3:
            file3.write(new_letter)


