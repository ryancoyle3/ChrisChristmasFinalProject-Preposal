import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {0: "Ace", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
         8: "9", 9: "10", 10: "Jack", 11: "Queen", 12: "King"}
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
    return draw1

#dealerDraw()


def players(playerNames):
        player = input("What are all of your names? \n (Seperate by space):").lower()
        player = player.split(" ")
        playerNames += player
        return player

#players(playerNames)

def getEntryBread(entryBread):
    
        
    

 
def phase1():
    firstHand = dealerDraw()
    return print("Dealers first hard is:", firstHand)

#phase1()    
        
def playAgain():
    choice = input("Enter 'Hit' to Hit or 'Stand' to Stand")
    if choice == "Hit":
        draw1()
    else:
        print("no")


#BET RULES
#min bet amount is $10    


#END GAME
#Ask for buy-in add to winnings and if winnings <= 0
#Players name is removed from list    


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

