import random
import art
from game_rules import how_to_play

"""
# Project 8: Blackjack Game
### Description:
This is a text-based implementation of the classic Blackjack game in Python. The game follows standard Blackjack rules, 
allowing players to hit or stand, and includes dynamic handling of Aces, dealer logic, and win conditions. Players 
can choose to replay the game after each round.

### Features:
- Text-based gameplay with player and dealer logic.
- Automatic Ace value adjustment (1 or 11) based on current score.
- Comprehensive win/bust checks for player and dealer.
- Continuous gameplay with replay functionality.
- Simplified, intuitive user interaction for hitting and standing.

# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-12-04
"""

print(art.logo)
print(how_to_play)
print("")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_card(list_name, score=0):
    card = random.choice(cards)

    if card == 11:
        if (score + card) > 21:
            print(f"Previous card value is {card}")
            card = 1
            print(f"Now new card value: {card}")
            list_name.append(card)
        else:
            list_name.append(card)
    else:
        list_name.append(card)


def win_check(p_score=0, d_score=0):
    if p_score > 21:
        print("You went over, you lose 😭")
        print(f"Your Final hand: {player_hand}, final score: {p_score}")
        print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
        print("")
        return True
    elif d_score > 21:
        print("You win, dealer's score went over 😊🙌😎")
        print(f"Your Final hand: {player_hand}, final score: {p_score}")
        print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
        print("")
        return True
    elif p_score == 21:
        print("Blackjack, you win! 😊🙌😎")
        print(f"Your Final hand: {player_hand}, final score: {p_score}")
        print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
        print("")
        return True
    elif d_score == 21:
        print("Blackjack, dealer wins 😭")
        print(f"Your Final hand: {player_hand}, final score: {p_score}")
        print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
        print("")
        return True


def final_win(p_score, d_score):
    if p_score < 21 and d_score < 21:
        if p_score > d_score:
            print(f"Your Final hand: {player_hand}, final score: {p_score}")
            print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
            print("You win! 😊🙌😎")
        elif p_score < d_score:
            print(f"Your Final hand: {player_hand}, final score: {p_score}")
            print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
            print("You lose 😭")
        else:
            print(f"Your Final hand: {player_hand}, final score: {p_score}")
            print(f"Dealer's Final hand: {dealer_hand}, final score: {d_score}")
            print("This is draw. 😜🤦‍♂️👀")


# game_on = game_on_off()

def playing_game():
    print("\n" * 30)
    print(art.logo)

    global player_hand
    global dealer_hand

    player_hand = []
    pl_score = 0
    dealer_hand = []
    de_score = 0

    for r in range(2):
        add_card(player_hand, pl_score)
        add_card(dealer_hand, de_score)

    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {dealer_hand[0]}")  # dealer's score: {dealer_score}

    if win_check(player_score, dealer_score):
        # game_on = False
        return

    while True:

        hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        print("")

        if hit_or_pass == "y":
            add_card(player_hand, player_score)
            player_score = sum(player_hand)
            print(f"Your Cards: {player_hand}, current score: {player_score}")
            print("")

            if win_check(player_score, dealer_score):
                return

        elif hit_or_pass == "n":
            while dealer_score < 16:
                add_card(dealer_hand, dealer_score)
                dealer_score = sum(dealer_hand)
                print(f"Dealer Cards: {dealer_hand}, current score: {dealer_score}")
                if win_check(player_score, dealer_score):
                    return
            break

    final_win(player_score, dealer_score)


player_hand = []
# # player_score = 0
dealer_hand = []
# # dealer_score = 0

while True:
    if input("Do you want to play again the Blackjack game, type 'Y' or 'N' --  ").upper() == "Y":
        playing_game()
    else:
        print("Goodbye! 👋😢 Hope to see you again as soon as possible 😊")
        break
