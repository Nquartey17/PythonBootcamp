import random

word_list = ["aardvark", "baboon", "camel"]

# Choose word from list
hang_word = word_list[random.randint(0,2)]
print(hang_word)

# Ask user to guess lowercase letter
character_guess = input("Guess a lowercase letter: ")

for letter in hang_word:
    if letter == character_guess:
        print("Right")
    else:
        print("Wrong")
