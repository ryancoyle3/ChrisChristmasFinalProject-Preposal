#Vincent Schetroma, Chris Christmas, Ryan Coyle

import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {0: "Ace", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
         8: "9", 9: "10", 10: "Jack", 11: "Queen", 12: "King"}



#Create an empty dictionary in the global space called cards delt, 
#which tracks the cards delt
#While not in cards delt pull from draw2
#Phase1: deal one card to every player
#Create a list players and use whiles to remove them once they stand



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
    Firstcard = []
    while len(Firstcard) < 2:
        cards = random.randint(0,12)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        Firstcard.append(card)
        Firstcard.append(suit)
    print("The card is", Firstcard)
        
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


def BlackJack():
    phase1()
    done = False
    while not done:
        winnigs = 0
        betAmount = input("How much are you willing to bet?")
        hand = draw2()
        dealersHand = dealerDraw()
        handAmount = 18 #(int(hand[0]) + int(hand[2]))
        dealerAmount = 17 #dealersHand[0] + dealersHand[2]
        while dealerAmount <= 16:
            addedCard = draw1()
            dealerAmount += addedCard
            if dealerAmount >= 17:
                print("The Dealer stands at",dealerAmount)
                continue
            elif dealerAmount > 21:
                print("The Dealer lost, you win.")
                done = True
        if handAmount > 21:
            print("You lose")
            done = True
            playAgain()
        elif handAmount == 21:
            print("You Win!!\n", betAmount *2)
            done = True
            playAgain()
        elif dealerAmount > 21:
            winnings += betAmount * 2
            print("You win, ", betAmount * 2, "congratulations!")
            done = True
            playAgain()

        
#draw1()
BlackJack()

