import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {0: "Ace", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
         8: "9", 9: "10", 10: "Jack", 11: "Queen", 12: "King"}

#Create an empty dictionary in the global space called cards delt, 
#which tracks the cards delt
#While not in cards delt pull from draw2
#Phase1: deal one card to every player
#Create a list players and use whiles to remove them once they stand

def draw1():
    hand = []
    while len(hand) < 2:
        cards = random.randint(0,12)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        hand.append(cards)
        hand.append(suit)
    print(hand)
#draw1()    

def draw2():
    hand = []
    while len(hand) < 4:
        cards = random.randint(0,12)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        hand.append(cards)
        hand.append(suit)
    print(hand)

#draw2()


def dealerDraw():
    return draw2()

#dealerDraw()

 
def phase1():
    one = []
    while len(one) < 2:
        cards = random.randint(0,12)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        one.append(card)
        one.append(suit)
    print("The card is",one)
        
def playAgain():
    choice = input("Enter 'Hit' to Hit or 'Stand' to Stand")
    if choice == "Hit":
        draw1()
    else:
        print("no")

    #if hand >= 16:
    #    print("yes")
    #else:
    # 3   print("no")

#BET RULES
#min bet amount must be divisible by $10 


#END GAME
#Ask for buy-in add to winnings and if winnings <= 0
#Players name is removed from list    

#If the dealers hand is 17 or greater the delater must stand
#if the dealers hand is 16 or smaller the dealer must hit
"""
def BlackJack():
    phase1()
    done = False
    while not done:
        winnigs = 0
        betAmount = input("How much are you willing to bet?")
        hand = draw2()
        dealersHand = dealerDraw()
        handAmount = int(hand[0] + hand[2])
        dealerAmount = dealersHand[0] + dealersHand[2]
        if handAmount > 21:
            print("You lose")
            done = True
            playAgain()
        elif handAmount = 21:
            print("You Win!!\n", betAmount *2)
            done = True
            playAgain()
        elif dealersAmount > 21:
            winnings += betAmount * 2
            print("You win, ", betAmount * 2, "congratulations!")
            done = True
            playAgain()

        
#BlackJack()
"""

#We draw two hard from the deck
#onces cards are drawn they must be removed from the deck
#Input print hit or stand
#Repeat until over 21 or at 21
#If hand > 21 you lose.

