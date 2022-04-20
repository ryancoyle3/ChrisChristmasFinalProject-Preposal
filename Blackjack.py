import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
         9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}
usedCardsTotal = []

usedCardsPlayer = []

usedCardsDealer = []

playerNames = []

entryBread = []

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
    
#draw2()

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
    print("The dealers first card is", dealerHand)
    return dealerHand

#dealerDraw()

  
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
        #use the validCard function
        hand.append(cards)
        hand.append(suit)
    return hand

#draw1()    



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
        return None


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
        dealerAmount = getValue(int(dealerHand[0])) #+ getValue(int(dealerHand[1]))
       # hit = hitOrStand()
        
            #handAmount += getValue(addedCard[0])
            #print("Your hand total is now",handAmount)
            #if handAmount > 21:
           #     winnings = winnings - betAmount
            #    print("Your hand total is greater than 21, the Dealer wins. :(")
             #   print("Your win total is now",winnings)
        while dealerAmount <= 16:
            addedCard = draw1()
            dealerAmount += getValue(addedCard[0])
            print("The Dealer hits to get",dealerAmount)
            if dealerAmount >= 17 and dealerAmount <= 21:
                print("The Dealer stands at",dealerAmount)
                continue
            elif dealerAmount > 21:
                winnings = betAmount + winnings
                print("The Dealer lost, you win!")
                print("Your win total is now",winnings)
                done = True
                break
        if 16 <= dealerAmount <= 21:
            addedCard = hitOrStand()
            if addedCard == None:
                break
            handAmount += getValue(addedCard[0])
            print("Your hand total is now",handAmount)
            if handAmount > 21:
                winnings = winnings - betAmount
                print("Your hand total is greater than 21, the Dealer wins. :(")
                print("Your win total is now",winnings)
                
                break
        if handAmount <= 21 and handAmount > dealerAmount:
            winnings = winnings + betAmount
            print("The Dealer loses you win!")
            print("Your win total is now",winnings)
            
        elif handAmount > 21:
            print("You lose")
            done = True
        elif handAmount == 21:
            print("You Win!!\n", betAmount *2)
            done = True
        elif dealerAmount > 21:
            winnings += betAmount
            print("You win, ", betAmount, "congratulations!")
            done = True
       #Have to move around the order of the game, look at online blackjack
        #simulator

        

blackJack()
