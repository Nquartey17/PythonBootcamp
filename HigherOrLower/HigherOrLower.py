import art
import game_data
import random

game_over = True
data_size = len(game_data.data) - 1
score = 0

def number_generator():
    return random.randint(0, len(game_data.data))

# def sentence(subject):
#     return (game_data.data[subject]['name'], " a ", game_data.data[subject]['description'], "from "
#                 ,game_data.data[sub1_num]['country'])

# Outside while loop, will get replaced as rounds continue
sub1_num = number_generator()

#while loop code
while game_over:
    print(art.logo)
    sub2_num = number_generator()

    #avoid duplicates
    while sub2_num == sub1_num:
        subject_2 = random.randint(0, len(game_data.data))

    print(f"Compare A: {game_data.data[sub1_num]['name']}, a {game_data.data[sub1_num]['description']}, from {game_data.data[sub1_num]['country']}")
    print(art.vs)
    print(f"Against B: {game_data.data[sub2_num]['name']}, a {game_data.data[sub2_num]['description']}, from {game_data.data[sub2_num]['country']}")

    answer = input("Who has more followers? 'A' or 'B'? ")

    # Turn into a function
    if game_data.data[sub1_num]["follower_count"] > game_data.data[sub2_num]["follower_count"]:
        if answer == "A":
            score += 1
            print(f"Correct! Your current score is {score}")
        else:
            print(f"Wrong answer, game over. Your final score is {score}")
            game_over= False
    else:
        if answer == "B":
            score += 1
            print(f"Correct! Your current score is {score}")
            sub1_num = sub2_num
        else:
            print(f"Wrong answer, game over. Your final score is {score}")
            game_over = False