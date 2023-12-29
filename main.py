############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random, os

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

game_play = True
while game_play:
    print(logo)



    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random_card = random.choice(cards)
        return random_card

    def calculate_score(cards_in_deck):
        card_total = 0
        card_total = sum(cards_in_deck)
        for num in range(len(cards_in_deck)):
            if (cards_in_deck[num] == 11):
                if (card_total > 21):
                    cards_in_deck.remove(11)
                    cards_in_deck.append(1)
                    card_total = sum(cards_in_deck)

        if (card_total == 21):
            return 0
        else:
            return card_total


    def compare(user, computer):
        if (user == 0 and computer == 0):
            return "Draw"
        elif (computer == 0):
            return "Computer wins!"
        elif (user == 0):
            return "You win!"
        elif (user > 21):
            return "Computer wins!"
        elif (computer > 21):
            return "You win!"
        elif (user == computer):
            return "Draw"
        else:
            if user > computer:
                return "You win!"
            else:
                return "Computer wins!"
    def display():
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    user_cards = []
    computer_cards = []

    for num in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[1]}")

    

    should_continue = True

    while should_continue:
        if (user_score == 0 and computer_score == 0):
            display()
            print("Computer wins!")
            should_continue = False
            break
        elif (computer_score == 0):
            display()
            print("Computer wins!")
            should_continue = False
            break
        elif (user_score == 0):
            display()
            print("You win!")
            should_continue = False
            break
        elif (user_score > 21):
            display()
            print("Computer wins!")
            should_continue = False
            break
        else:
            if(input("Would you like another card? yes or no?: ") == "no"):
                while (computer_score < 17):
                    computer_cards.append(deal_card())
                    print(f"Computer: {computer_cards}")
                    computer_score = calculate_score(computer_cards)
                    print(computer_score)
                display()
                print(compare(user_score, computer_score))
                break
            else:         
                user_cards.append(deal_card())
                print(f"Your cards: {user_cards}")
                user_score = calculate_score(user_cards)
                print(user_score)
    if (input("Would you like to restart the game?: 'yes' or 'no': ") == "no"):
        print("The game has ended.")
        game_play = False
    else:
        clear_console()
