import random

word_list = ["aardvark", "baboon", "camel"]

# Choose word from list
hang_word = word_list[random.randint(0,2)]
print(hang_word)
placeholder = "_" * len(hang_word)
print(placeholder)

# Ask user to guess lowercase letter
character_guess = input("Guess a letter: ").lower()

display = ""
for letter in hang_word:
    if letter == character_guess:
        display += character_guess
    else:
        display += "_"

print(display)

