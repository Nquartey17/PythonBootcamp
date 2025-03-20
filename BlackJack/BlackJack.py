import art
import random

# The Ace can count as 11 or 1.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
max_score = 21

start_game = True
keep_drawing = True

player_cards = []
player_total = 0
computer_cards = []
computer_total = 0

def get_card():
    return random.choice(cards)

def total_score(selected_list):
    total_sum = 0
    for i in selected_list:
        total_sum = total_sum + i
    return total_sum

def print_player_score(selected_list, score ):
    print(f"Your cards: {selected_list}, current score: {score}")

while start_game:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_game == "y":
        player_cards.clear()
        computer_cards.clear()
        print(art.logo)

        # Get 2 cards for player and computer, Remember 11 can also be 1
        # ISSUE- ROUNDS ENDING AFTER FIRST DRAW
        player_cards.append(get_card())
        player_cards.append(get_card())
        player_total = total_score(player_cards)
        print_player_score(player_cards, player_total)

        computer_cards.append(get_card())
        computer_total = total_score(computer_cards)
        #Computer cards have to be above 17
        while computer_total < 17 :
            computer_cards.append(get_card())
            computer_total = total_score(computer_cards)
        print(f"Computer's first card: {computer_cards[0]}")

        #Keep asking this while score isn't over 21
        while keep_drawing and player_total <= 21:
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_again == "y":
                checked_value = get_card()
                if checked_value == 11 and (player_total + checked_value) > max_score:
                    player_cards.append(1)
                    player_total = total_score(player_cards)
                    print_player_score(player_cards, player_total)
                else:
                    player_cards.append(checked_value)
                    player_total = total_score(player_cards)
                    print_player_score(player_cards, player_total)
            else:
                keep_drawing = False

        #compare scores from player and computer
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        if player_total > 21:
            print("You went over 21, you lose")
        elif computer_total > 21:
            print("Computer went over 21, you win")
        elif player_total > computer_total:
            print("You win")
        elif computer_total > player_total:
            print("You lose")
        else:
            print("Draw")

    else:
        start_game = False