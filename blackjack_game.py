logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''
print(logo)

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random

def card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_scores(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "It's a tie! Both you and the computer have blackjack."
    if user_score==computer_score:
        return "It's a draw!!"
    elif computer_score==0:
        return "Lose, opponent has Blackjack!!"
    elif user_score==0:
        return "Win with a Blackjack!!"
    elif user_score > 21:
        return "You went over. You lose!!"
    elif computer_score > 21:
        return "Opponent went over. You win!!"
    elif user_score > computer_score:
        return "You win!!"
    else:
        return "You lose!!"
    
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(card())
        computer_cards.append(card())
    while not is_game_over:
        user_score=calculate_scores(user_cards)
        computer_score=calculate_scores(computer_cards)
        print(f"Your card: {user_cards} and Current scores: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(card())
        else:
            is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card())
        computer_score = calculate_scores(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()
        