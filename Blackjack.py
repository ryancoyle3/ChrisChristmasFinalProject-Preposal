import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
         9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}
usedCards = []

playerNames = []

entryBread = []
  
#Create an empty dictionary in the global space called cards delt, 
#which tracks the cards delt
#While not in cards delt pull from draw2
#Phase1: deal one card to every player
#Create a list players and use whiles to remove them once they stand

def draw1():
    hand = []
    while len(hand) < 2:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        hand.append(cards)
        hand.append(suit)
    return hand

#draw1()    

def draw2():
    hand = []
    while len(hand) < 4:
        cards = random.randint(1,13)
        color = random.randint(0,3)
        suit = suits[color]
        card = deck[cards]
        hand.append(cards)
        hand.append(suit)
    return hand
    

#draw2()


def dealerDraw():
    return draw2()

#dealerDraw()


def players(playerNames):
        player = input("What are all of your names? \n (Seperate by comma):").lower()
        player = player.split(",")
        playerNames += player
        print(playerNames)

#players(playerNames)

def getEntryBread(entryBread):
    for name in playerNames:
        money = input(name + ": How much do you want to bet?")
        money = money.split(" ")
        entryBread += money
        return entryBread
           
#getEntryBread(entryBread)

def playAgain():
    blackJack()
        
    

def hitOrStand():
    choice = input("Enter 'Hit' to Hit or 'Stand' to Stand").lower()
    if choice == "hit":
        return draw1()
    else:
        return null


#BET RULES
#min bet amount is $10    


#END GAME
#Ask for buy-in add to winnings and if winnings <= 0
#Players name is removed from list

def getValue(card):
    if card >= 2 and card <= 10:
        return card
    elif card > 10:
        return 10
    else:
        return 11        
      

def blackJack():
    done = False
    while not done:
        winnings = 0
        betAmount = int(input("How much are you willing to bet?"))
        while betAmount % 10 != 0:
            betAmount = int(input("Your bet amount must be in terms of 10."))
        dealerHand = dealerDraw()
        hand = draw2()
        handAmount = getValue(int(hand[0])) + getValue(int(hand[2]))
        dealerAmount = getValue(dealerHand[0]) + getValue(dealerHand[2])
        while dealerAmount <= 16:
            addedCard = draw1()
            dealerAmount += getValue(addedCard[0])
            if dealerAmount >= 17 and dealerAmount <= 21:
                print("The Dealer stands at",dealerAmount)
                continue
            elif dealerAmount > 21:
                print("The Dealer lost, you win.")
                done = True
        while handAmount True:
            hitOrStand()

        if handAmount > 21:
            print("You lose")
            done = True
        elif handAmount == 21:
            print("You Win!!\n", betAmount *2)
            done = True
        elif dealerAmount > 21:
            winnings += betAmount
            print("You win, ", betAmount * 2, "congratulations!")
            done = True
        

        

blackJack()

