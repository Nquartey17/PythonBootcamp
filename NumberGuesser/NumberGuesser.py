import art
import random

ANSWER = random.randint(1,100)
EASY = 10
HARD = 5
attempts = 0
user_guess = 0

#Game start
print(art.logo)
print("Welcome to the number guessing game!")
difficulty = input("Select difficult. Enter 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = EASY
elif difficulty == "hard":
    attempts = HARD

# keeping going while attempts aren't zero, or user hasn't guessed the right answer
while attempts > 0:
    print(f"You have {attempts} remaining.")
    guess = int(input("Make a guess: "))
    if guess == ANSWER:
        print(f"You guessed the correct answer, {ANSWER}")
        break
    elif guess > ANSWER:
        print("Guess is too high")
    else:
        print("Guess is too low")
    attempts -= 1

if attempts == 0:
    print(f"You lose, the correct answer was {ANSWER}")
