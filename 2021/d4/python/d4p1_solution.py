# Advent of Code - Day 4 Problem 1

class Player:
    def __init__ (self):
        self.card = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.marked = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {
            "row" : [0,0,0,0,0],
            "column": [0,0,0,0,0]
        }

# Takes in a player and the bingo number to update their marker card and row/column tracker
# and checks if the player has hit bingo. If so, the winningTotal() function is called.
def updateBingo(player, num):
    for y in range(5):
        for x in range(5):
            check = int(player.card[y][x])

            # Check if this position contains a hit 
            if check == num:

                # Update the bingo tracker
                player.bingo["row"][y] += 1
                player.bingo["column"][x] += 1

                # Update marked board
                player.marked[y][x] = "X"

                # Check if the player has now hit bingo from a winning row
                if player.bingo["row"][y] == 5: 
                    #End the game and print results
                    winningNumber = int(player.card[y][x])
                    total = winningTotal(player, winningNumber)

                    print("The total of the winning card is:", total)
                    exit()
                # Check if the player has now hit bingo from a winning column
                elif player.bingo["column"][x] == 5:
                    #End the game and print results
                    winningNumber = int(player.card[y][x])
                    total = winningTotal(player, winningNumber)

                    print("The total of the winning card is:", total)
                    exit()

# Calculates the winning Bingo card by adding up the numbers not marked and multiplying it by the winning number
def winningTotal(player, winningNumber):
    total = 0

    for y in range(5):
        for x in range(5):
            if player.marked[y][x] != "X":
                total += int(player.card[y][x])

    return total * winningNumber

# Starts the game by reading file to get players and their cards as well as well as the bingo numbers pulled
# Each player has their own card, a card keeping track of which numbers have been marked, and a row/column tracker
def startGame():
    inputFile = open ('../input/d4_input.txt','r')
    file = inputFile.readlines()

    playerNum = 0
    bingoNumbers = file[0].strip().split(",") # Read in the bingo numbers which is the first line of the file 
    numPlayers = int((len(file) - 1) / 6) # 6 is the bingo card size + 1 (to account for space between them in file input)
    player = []

    # Initialiaze all the players
    for i in range(numPlayers):
        player.append(Player())

    # Fill out boards by initializing players and filling their respective cards
    for i in range(2, len(file), 6):
        player[playerNum].card[0] = file[i].split()
        player[playerNum].card[1] = file[i + 1].split()
        player[playerNum].card[2] = file[i + 2].split()
        player[playerNum].card[3] = file[i + 3].split()
        player[playerNum].card[4] = file[i + 4].split()

        playerNum += 1

    # Run through the bingo Numbers and check each player's cards for bingo
    for i in range(len(bingoNumbers)):
        for j in range(numPlayers):
            updateBingo(player[j], int(bingoNumbers[i]))

    inputFile.close() 

startGame()