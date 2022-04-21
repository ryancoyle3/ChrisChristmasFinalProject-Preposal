import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
         9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}

usedCardsTotal = []

usedCardsPlayer = []

usedCardsDealer = []

playerNames = []

entryBread = []


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

def ace(handAmount):
    if sum(handAmount-1) == 21 or sum(handAmount+11) > 21:
        deck[1] = 1
    else:
        deck[1] = 11

def getValue(card):
    if card >= 1 and card <= 10:
        return card
    elif card > 10:
        return 10
    
def dealerDraw():
    dealerHand = []
    usedCardsDealer = []
    usedCardsTotal = []
    while len(dealerHand) < 2:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        #use the validCard function
        dealerHand.append(cards)
        dealerHand.append(suit)
        usedCardsTotal += dealerHand
        usedCardsDealer += dealerHand
    print("The dealers first card is", getValue(dealerHand[0]), dealerHand[1])
    return dealerHand

def draw2():
    hand = []
    usedCardsTotal = []
    usedCardsPlayer = []
    while len(hand) < 4:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        #use the validCard function
        hand.append(cards)
        hand.append(suit)
        usedCardsTotal += hand
        usedCardsPlayer += hand
    print("Your hand is",hand)
    return hand

    

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
        handAmount = getValue(int(hand[0])) + getValue(int(hand[2]))
        dealerAmount = getValue(int(dealerHand[0]))
        choice = input("Enter 'Hit' to Hit or 'Stand to Stand.").lower()
        while choice == 'hit':
            addedCard = draw1()
            handAmount += getValue(addedCard[0])
            print("Your hand amount is now", handAmount)
            if handAmount > 21:
                print("Your hand amount is over 21, The Dealer wins.")
                break
            choice = input("Enter 'Hit' to Hit or 'Stand' to Stand").lower()  
        else:
                print("The Dealers hand amount is",dealerAmount)
                print("Your hand amount is", handAmount)
        if handAmount <= 21 and handAmount > dealerAmount:
            winnings = winnings + betAmount
            print("The Dealer loses, you win!")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif dealerAmount > handAmount:
            winnings = winnings - betAmount
            print("The Dealer won you lose. :[")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif handAmount > 21:
            winnings = winnings - betAmount
            print("The Dealer won, you lose", ":(")
            print("Your win total is now", winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif handAmount == 21:
            winnings = winnings - betAmount
            print("The Dealer loses you win!")
            print("Your win total is now",winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True
        elif dealerAmount > 21:
            winnings = winnings + betAmount
            print("The Dealer loses you win!")
            print("Your win total is now", winnings)
            playagain = input("Enter yes to play again.")
            if playagain == 'yes':
                done = done
            else:
                done = True

    done = True
        
            
            
blackjack()
