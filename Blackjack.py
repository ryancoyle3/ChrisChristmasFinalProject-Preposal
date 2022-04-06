import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = {0: "Ace", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
         8: "9", 9: "10", 10: "Jack", 11: "Queen", 12: "King"}


def draw2():
    cards = random.randint(0,12)
    card = deck[cards]
    hand = []
    while card == 2:
        hand += card
        print(hand)
        

draw2()        

"""
def part1():
    turn = 0
    done = False
    while not done:
        result = roll2()
        print("Hand", result)
        if result >= 21:
            turn = 0
            done = True
        else:
            turn += 1    

    return turn
part1()
"""
"""
def part2(turns):
    outcomes = {}
    outcomes[0] = 0
    for score in range(20,26):
        outcomes[score] = 0
    for _ in range(turns):
        turnScore = part1()
        outcomes[turnScore] += 1
    print("Score\tProbability")
    for score in outcomes:
        print(score,str(outcomes[score]/turns*100)+"%",sep="\t")

def holdAtXTurn(holdValue):
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        #print("Roll:",result)
        if result == 1:
            turnScore = 0
            done = True
        else:
            turnScore = turnScore + result
            if turnScore >= holdValue:
                done = True
    #print("Turn Score:", turnScore)
    return turnScore


def part3(turns, holdValue):
    outcomes = {}
    outcomes[0] = 0
    for score in range(holdValue,holdValue+6):
        outcomes[score] = 0

    for _ in range(turns):
        turnScore = holdAtXTurn(holdValue)
        outcomes[turnScore] += 1
    print("Score\tProbability")
    for score in outcomes:
        print(score,str(outcomes[score]/turns*100)+"%",sep="\t")

#part3(1000000,100)

def part4():
    score = int(input("Score?"))
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        print("Roll:",result)
        if result == 1:
            turnScore = 0
            done = True
        else:
            turnScore += result
            newScore = score + turnScore
            if turnScore >= 20:
                done = True
    print("Turn Score:", turnScore)
    print("New Score:" , score + newScore)
#part4()

def part5():
    turnScore = 0
    score = 0
    newScore = 0
    while newScore < 100:
        result = rolld6()
        print("Roll:",result)
        if result == 1:
            turnScore = 0
            newScore = 0
            print("Turn Score:", turnScore)
            print("New Score:" , newScore)
        else:
            turnScore += result
        if turnScore >= 20:
            newScore += turnScore
            turnScore = 0
            print("Turn Score:", turnScore)
            print("New Score:" , newScore)
        if newScore >= 100:
            print("Turn Score:", turnScore)
            print("New Score:" , newScore)
            break
            
#part5()

def part6(games):
    turnScore = 0
    score = 0
    newScore = 0
    count = 0
    while newScore < 100:
        result = rolld6()
        #print("Roll:",result)
        if result == 1:
            turnScore = 0
            newScore = 0
        else:
            turnScore += result
            count += 1
        if turnScore >= 20:
            newScore += turnScore
            turnScore = 0
        if newScore >= 100:
            print("Average Games:", games / count)
            break
games = int(input("How many games have you played?"))
part6(games)

def part7():
    player1score = 0
    player2score = 0
    n = 0
    while True:
        print("Player 1 score:", player1score)
        print("Player 2 score:", player2score)
        if n==0:                                            
            turnScore =0
            print("It is player 1's turn.")
            while turnScore <= 20 and (turnScore + player1score) <=100:
                roll = rolld6()   
                print("Roll :",roll)
                if roll == 1:
                    turnScore = 0
                    player1score = 0
                    break
                turnScore = turnScore + roll
                if turnScore >= 20:
                    turnScore = turnScore
                    break
                if (turnScore + player1score) >= 100:
                    break
            player1score += turnScore               
            print("Turn Score :",turnScore)
            print("New Score :",player1score)
            n=1
        elif n==1:                                          
            turnScore = 0
            print("It is player 2's turn.")
            while turnScore <= 20 and (turnScore + player2score) <=100:
                roll = rolld6()        
                print("Roll:",roll)
                if roll == 1:
                    turnScore = 0
                    player2score = 0
                    break
                turnScore = turnScore + roll
                if turnScore >= 20:
                    turnScore = turnScore
                    break
                if (turnScore + player2score) >=100:
                    break
           
            player2score += turnScore             
            print("Turn Score :",turnScore)
            print("New score :",player2score)
            n=0
        if player1score >= 100 or player2score >= 100:
            break
  
#part7()

random.seed()

def cpu():
    turnTotal = 0
    while True:
        roll = rolld6()
        print("Roll: %d" %roll)
        if roll == 1:
            turnTotal = 0
            print("Turn total: %d" %turnTotal)
            break
        else:
            turnTotal += roll
        if turnTotal >= 20:
            print("Turn total: %d" %turnTotal)
            break

    return turnTotal

def Player():
    turnTotal = 0
    choice = input("Roll/Hold?")
    while choice =="":
        roll = rolld6()
        print("Roll: %d" %num)
        if roll == 1:
            turnTotal = 0
            print("Turn total: %d" %turnTotal)
            break
        
        else:
            turnTotal += num
            choice = input("Turn total: %d Roll/Hold? (Enter)" %(turnTotal))
            if turnTotal >= 20:
                print("Turn total : %d" %turnTotal)
                break

    return turnTotal

def part8():
    playernumber = random.randint(0,1)
    comp = 1 - playernumber
    print("You will be Player %d" %(playernumber+1))
    print("Enter nothing to roll; anything to hold.")
    score = [0, 0]
    i = 0
    while True:
        print("Player 1 score: %d" %score[0])
        print("Player 2 score: %d" %score[1])
        print("It is Player %d's turn" %((i%2)+1))
        if i == comp:
            score[i] += cpu()
        else:
            score[i] += Player()
        print("New score: %d" %score[i])
        i = (i + 1)%2
        if score[0] >= 100 or score[1] >= 100:

            break


#part8()
"""

