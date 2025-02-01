
import random
from art import logo

print("HELLO TO SIMPLIFIED BLACKJACK, THESE ARE THE RULES:")
print(
"The deck is unlimited in size.\nThere are no jokers.\nThe Jack/Queen/King all count as 10."
)
print(
    "There are no jokers.\nThe Jack/Queen/King all count as 10.\nThe the Ace can count as 11 or 1."
)
print("The following list is the deck of cards:\ncards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]"
)
print("The cards in the list have equal probability of being drawn.\nCards are not removed from the deck as they are drawn")
print("Try to your score closer to 21 than the dealer!, however if your score goes over 21 you LOSE!")



def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'hit' to get another card, type 'stand' to pass: ")
            if user_should_deal == "hit":
                user_cards.append(deal_card())
            elif user_should_deal == "stand":
                is_game_over = True
            elif user_should_deal != "hit" and user_should_deal != "stand":
              raise TypeError
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    for a in range(1, 100):
        print(" ")
    play_game()


