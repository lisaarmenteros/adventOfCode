# Advent of Code - Day 4 Problem 2 

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

class Winners:
    def __init__ (self):
        self.winnersIndex = []
        self.winnersList = []
        self.winningNumber = []

# Takes in a player and the bingo number to update their marker card and row/column tracker
# and checks if the player has hit bingo. 
def updateBingo(player, num, winners):
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
                    # Add winning number for winners
                    winningNumber = int(player.card[y][x])
                    winners.winningNumber.append(winningNumber)
                    # Add winning player to winners list
                    winners.winnersList.append(player)
                    return True

                # Check if the player has now hit bingo from a winning column
                elif player.bingo["column"][x] == 5:
                    # Add winning number for winners
                    winningNumber = int(player.card[y][x])
                    winners.winningNumber.append(winningNumber)
                    # Add winning player to winners list
                    winners.winnersList.append(player)
                    return True

    return False

# Calculates the winning Bingo card by adding up the numbers not marked and multiplying it by the winning number
def winningTotal(winner, winningNumber):
    total = 0

    for y in range(5):
        for x in range(5):
            if winner.marked[y][x] != "X":
                total += int(winner.card[y][x])
            
    return total * winningNumber

# Starts the game by reading file to get players and their cards as well as well as the bingo numbers pulled
# Each player has their own card, a card keeping track of which numbers have been marked, and a row/column tracker
def startGame():
    inputFile = open ('../input/d4_input.txt','r')
    file = inputFile.readlines()

    playerNum = 0
    player = []
    winners = Winners()
    bingoNumbers = file[0].strip().split(",") # Read in the bingo numbers which is the first line of the file 
    numPlayers = int((len(file) - 1) / 6) # 6 is the bingo card size + 1 (to account for space between them in file input)

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
            haveWinner = updateBingo(player[j], int(bingoNumbers[i]), winners)
            # If there is a winner, append their indexes to winnerIndex list for deletion
            if(haveWinner):
                winners.winnersIndex.append(j)
                playerNum -= 1
        # Update the number of players left and delete the players which have already won
        numPlayers = playerNum
        for k in range(len(winners.winnersIndex)):
            # Delete numbers from largest index to smallest index
            del player[winners.winnersIndex[len(winners.winnersIndex)-1-k]]
        winners.winnersIndex.clear()
        
    # Get the last card to win bingo and calculate solution
    total = winningTotal(winners.winnersList[-1], winners.winningNumber[-1])
    print("The total of the winning card is:", total)

    inputFile.close() 

startGame()