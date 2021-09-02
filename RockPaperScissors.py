import random
global humanScore
global botScore
humanScore = 0
botScore = 0

def rpsBot():
    global botTurn
    botTurn = random.randint(1, 3)
    if botTurn == 1:
        botTurn = 'rock'
    elif botTurn == 2:
        botTurn = 'scissors'
    elif botTurn == 3:
        botTurn = 'paper'
    else:
        print("brian youre stupid its still broken")

def humanTurn():
    print("'Rock', 'Paper', or 'Scissors'?")
    humanTurn = input()
    if humanTurn.lower() == 'rock':
        if botTurn == 'rock':
            print("Bot played 'Rock'")
            print("Tie.")
        elif botTurn == 'scissors':
            print("Bot played 'Scissors'")
            print("You win!")
            global humanScore
            global botScore
            humanScore += 1
        elif botTurn == 'paper':
            print("Bot played 'Paper'")
            print("You lose.")
            botScore += 1

    elif humanTurn.lower() == 'scissors':
        if botTurn == 'rock':
            print("Bot played 'Rock'")
            print("You lose.")
            botScore += 1
        elif botTurn == 'scissors':
            print("Bot played 'Scissors'")
            print("Tie.")
        elif botTurn == 'paper':
            print("Bot played 'Paper'")
            print("You win!")
            humanScore += 1

    elif humanTurn.lower() == 'paper':
        if botTurn == 'rock':
            print("Bot played 'Rock'")
            print("You win!")
            humanScore += 1
        elif botTurn == 'scissors':
            print("Bot played 'Scissors'")
            print("You lose.")
            botScore += 1
        elif botTurn == 'paper':
            print("Bot played 'Paper'")
            print("Tie.")


def playGame():
    while True:
        rpsBot()
        botTurn = rpsBot()
        print("The score is currently You:" + str(humanScore) + " - Computer:" + str(botScore) + ".")
        humanTurn()
        if humanScore == 4:
            print("You win the game!")
            playAgain()
        elif botScore == 4:
            print("You lose the game. :(")
            playAgain()

def playAgain():
    print("Would you like to play again? 'Yes' or 'No'?")
    playAgain = input()
    if playAgain.lower() == 'yes':
        global botScore
        global humanScore
        humanScore = 0
        botScore = 0
        playGame()
    elif playAgain.lower() == 'no':
        print("Okay.")
    else:
        playAgain()

playGame()
