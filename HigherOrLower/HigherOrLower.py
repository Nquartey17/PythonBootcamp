import art
import game_data
import random

game_over = True
data_size = len(game_data.data) - 1
score = 0

# 0 - name
# 1 - follower_count
# 2 - description
# 3 - country

def number_generator():
    return random.randint(0, len(game_data.data))



# Outside while loop, will get replaced as rounds continue
sub1_num = number_generator()

print(art.logo)

sub2_num = number_generator()

#avoid duplicates
while sub2_num == sub1_num:
    subject_2 = random.randint(0, len(game_data.data))

print(art.logo)
print(f"Compare A: {game_data.data[sub1_num]['name']}, a {game_data.data[sub1_num]['description']}, from {game_data.data[sub1_num]['country']}")
print(art.vs)
print(f"Against B: {game_data.data[sub2_num]['name']}, a {game_data.data[sub2_num]['description']}, from {game_data.data[sub2_num]['country']}")