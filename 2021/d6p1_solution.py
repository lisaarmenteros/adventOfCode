# Advent of Code - Day 6 Problem 1

inputFile = open ('input/d6_input.txt','r')
lines = inputFile.readlines()
lines = lines[0].split(",")

total = 0

ageOfFish = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [8, 0]
]

# Store the number of each age of fish
for i in range(len(lines)):
    ageOfFish[int(lines[i])][1] += 1

# Cicle through 80 days
for i in range(80):
    # If there are a number of fishes with age zero, add this number of fish at age 8 and age 6 after decreasing the age of fish by one
    # This is accomplished by shifting the ages down
    if ageOfFish[0][1] > 0:
        numZeros = ageOfFish[0][1]
        for j in range(8):
            ageOfFish[j][1] = ageOfFish[j + 1][1]
        ageOfFish[8][1] = numZeros
        ageOfFish[6][1] += numZeros
    # If there are no zeros, just decrease the ages of fish by one
    # This is accomplished by shifting the ages down and setting the number of fish with age 8 to zero
    else: 
        for j in range(8):
            ageOfFish[j][1] = ageOfFish[j + 1][1]
        ageOfFish[8][1] = 0

for i in range(9):
    total += ageOfFish[i][1]

print(total)

inputFile.close()