import random

user_number = int(input("What do you choose? 0 = Rock, 1 = Paper, 2 = Scissors "))
comp_number = random.randint(0,2)

if user_number < 0 or user_number > 2:
    print("Invalid number, you lose")

print("Computer chose: ")
if comp_number == 0:
    print("Rock")
elif comp_number == 1:
    print("Paper")
else:
    print("Scissors")

if user_number == comp_number:
    print("Draw")
elif (user_number == 1 and comp_number == 0) or (user_number == 2 and comp_number == 1) or (user_number == 0 and comp_number == 2):
    print("You win")
else:
    print("You lose")
