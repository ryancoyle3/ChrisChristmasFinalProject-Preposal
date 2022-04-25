import random

suits = ["Club ︎♣︎", "Diamond ♦︎", "Heart ♥︎", "Spade ♠︎"]

deck = {1: "Ace🂱", 2: "2🂲", 3: "3🂳", 4: "4🂴", 5: "5🂵", 6: "6🂶", 7: "7🂷", 8: "8🂸",
         9: "9🂹", 10: "10🂺", 11: "Jack🂻", 12: "Queen🂽", 13: "King🂾"}

usedCardsTotal = []

usedCardsPlayer = []

usedCardsDealer = []

playerNames = []

entryBread = []

def ace(handAmount):
    if sum(handAmount) > 21 and 11 in handAmount:
        index = handAmount.index(11)
        handAmount[index] = 1
  #Changes an Ace into either 1 or 11 based on the handAmount

def draw1():
    hand = []
    while len(hand) < 2:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        #use the validCard function
        hand.append(cards)
        hand.append(suit)
    return hand
#print(draw1())

    #Used to draw one card, called upon hit being entered

def getValue(card):
    if card >= 1 and card <= 10:
        return card
    elif card > 10:
        return 10

    #Determines the number value of the card
    
def dealerDraw():
    dealerHand = []
    dealerHaand = []
    usedCardsDealer = []
    usedCardsTotal = []
    while len(dealerHand) < 2:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        #use the validCard function
        dealerHand.append(cards)
        dealerHaand.append(card)
        dealerHaand.append(suit)
        dealerHand.append(suit)
        usedCardsTotal += dealerHand
        usedCardsDealer += dealerHand
    print("The dealers first card is", dealerHaand)
    return dealerHand

    #Deals the first card of the Dealers hand without showing the second one

def draw2():
    hand = []
    haand = []
    usedCardsTotal = []
    usedCardsPlayer = []
    while len(hand) < 4:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        #use the validCard function
        haand.append(card)
        haand.append(suit)
        hand.append(cards)
        hand.append(suit)
        usedCardsTotal += hand
        usedCardsPlayer += hand
    print("Your hand is",haand)
    return hand

    #Draws the first two cards in the players hand


def blackjack():
    done = False
    winnings = 0
    while not done:
        betAmount = int(input("How much are you willing to bet?"))
        while betAmount % 10 != 0:
            print("Your bet amount must be in terms of 10.")
            betAmount = int(input("How much are you willing to bet?"))
        dealerHand = dealerDraw()       
        hand = draw2()
        handAmount = []
        handAmount.append(getValue(int(hand[0])))
        handAmount.append(getValue(int(hand[2])))
        dealerAmount = getValue(int(dealerHand[0]))
        choice = input("Enter 'Hit' to Hit or 'Stand to Stand.").lower()
        while choice == 'hit':
            addedCard = draw1()
            handAmount.append(getValue(addedCard[0]))
            ace(handAmount)
            print("Your hand amount is now", sum(handAmount))
            if sum(handAmount) > 21:
                print("Your hand amount is over 21, The Dealer wins.")
                done = True
                break
            choice = input("Enter 'Hit' to Hit or 'Stand' to Stand").lower()
        if sum(handAmount) > 21:
            winnings = winnings + betAmount
            print("The Dealer loses, you win! 💰🍾")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True          
        if dealerAmount < 16 or dealerAmount == handAmount:
            addedCard = draw1()
            dealerAmount += getValue(addedCard[0])
            print("The Dealers hand amount is",dealerAmount)
        print("Your hand amount is", sum(handAmount))
        if sum(handAmount) <= 21 and sum(handAmount) > dealerAmount:
            winnings = winnings + betAmount
            print("The Dealer loses, you win! 💰🍾")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif sum(handAmount) > 21:
            winnings = winnings - betAmount
            print("The Dealer won, you lose. 🤡")
            print("Your win total is now", winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif sum(handAmount) == 21:
            winnings = winnings - betAmount
            print("The Dealer loses you win! 💰🍾")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif dealerAmount > 21:
            winnings = winnings + betAmount
            print("The Dealer loses you win! 💰🍾")
            print("Your win total is now", winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif dealerAmount > sum(handAmount) and dealerAmount < 22:
            winnings = winnings - betAmount
            print("The Dealer won you lose. 🤡")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True

    done = True
        
        #Full Blackjack function 
            
blackjack()
