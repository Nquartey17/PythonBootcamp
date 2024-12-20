print("Welcome to Treasure Island.\nYour missions is to find the treasure")
direction = input("left or right? ")
if direction == "left" or direction == "l":
    movement = input("Swim or wait? ")
    if movement == "wait":
        doors = input("Which door will you take? Red, Blue, or Yellow? ")
        if doors == "red" or doors == "r":
            print("Burned by fire. Game over")
        elif doors == "yellow" or doors == "y":
            print("You win!")
        elif doors == "blue" or doors == "b":
            print("Eaten by beasts. Game over")
        else:
            print("Invalid response. Game over")
    else:
        print("You were attacked by a trout. Game Over")
else:
    print("You fell into a hole. Gave Over")
