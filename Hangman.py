import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


word_length = len(chosen_word)
placeholder = "_" * word_length
print(placeholder)

count = 0
new_display = ""
correct_letters = []

while count < word_length:
    guess = input("Guess a letter: ").lower()
    count += 1
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("You win")
        break

