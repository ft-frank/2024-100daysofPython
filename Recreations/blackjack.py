import random

deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def draw():
    return random.choice(deck)




player = []
dealer = []
player.append(draw())
player.append(draw())
dealer.append(draw())
dealer.append(draw())
playing = True
while playing:
    print(f"Your hand is: {player}")
    print(f"score = {sum(player)}")
    print(f"Dealer's first card: {dealer[0]}")
    decision = input("Do you wish to 'hit' or to 'stand' ").lower()
    if decision == "hit":
        player.append(draw())
        if sum(player) > 21:
            playing = False
    else:
        playing = False

print(f"final score = {sum(player)}")
print(f"Dealer's final score: {dealer}")
if sum(player) > 21:
    print("you bust")
elif sum(dealer) > 21:
    print("you win. dealer busted")
elif sum(dealer) > sum(player):
    print("dealer wins")
elif sum(player) > sum(dealer):
    print("player wins")
elif sum(player) == sum(dealer):
    print("chop!")



