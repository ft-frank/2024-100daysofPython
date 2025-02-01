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
print("The cards in the list have equal probability of being drawn.\nCards are not removed from the deck as they are drawn.\n")
print("Try to your score closer to 21 than the dealer!, however if your score goes over 21 you LOSE!")





def Blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def draw():
        return cards[random.randint(0, len(cards) - 1)]


    # INITIATIon
    hand = []
    hand.append(draw())
    hand.append(draw())
    dealer = []
    dealer.append(draw())
    dealer.append(draw())
    while sum(hand) > 21:
        for x in hand:
            if x == 11:
                hand[hand.index(x)] = 1
    print(f"  Your cards: {hand}, current score = {sum(hand)}")
    print(f"  Computer's first card: {dealer[0]}")
    decision = input("Do you wish to 'hit' or to 'stand'? ").lower()

    if decision != 'hit' and decision != 'stand':
        raise TypeError

    # HIT
    if decision == "hit":
        hit = True
    else:
        hit = False
    while hit == True:
            hand.append(draw())
            while sum(hand) > 21:
                for x in hand:
                    if x == 11:
                        hand[hand.index(x)] = 1
                hit = False
            if sum(hand) > 21:
                hit = False
            print(f"  Your cards: {hand}, current score = {sum(hand)}")
            print(f"  Computer's first card: {dealer[0]}")
            decision = input("Do you wish to 'hit' or to 'stand'? ").lower()



    while sum(dealer) < 17:
        dealer.append(draw())
    while sum(dealer) > 21:
        for x in dealer:
            if x == 11:
                dealer[dealer.index(x)] = 1
            else:
                break
        break

    #Who Wins?
    print(f"  Your final hand: {hand}, final score: {sum(hand)} ")
    print(f"  Computer's final hand: {dealer}, final score: {sum(dealer)} ")
    if sum(hand) > 21:
        print("YOU BUSTED")
    elif sum(dealer) > 21:
        print("YOU WIN, Dealer")
    elif sum(hand) > sum(dealer):
        print("YOU WIN")
    elif sum(hand) < sum(dealer):
        print("YOU LOSE")
    elif sum(hand) == sum(dealer):
        print("DRAW")
    again = input("Do you want to play another game of Blackjack? Type 'yes' or 'no' ").lower()
    if again == "yes":
        for x in range(100):
            print(" ")
        Blackjack()


Blackjack()

