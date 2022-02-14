# Advent of Code - Day 9 Problem 1

# Calculate the risk level by adding 1 to the low point and adding them together
def calculateRiskLevel(lowPoints):
    riskLevel = 0
    for i in range(len(lowPoints)):
        riskLevel += (lowPoints[i] + 1)

    return riskLevel

inputFile = open ('../input/d9_input.txt','r')
lines = list(inputFile.readlines())
lowPoints = []

# Split line of numbers into their own sublist
for i in range(len(lines)):
    lines[i] = list(map(int, list(lines[i].strip())))

# Run throught the list of numbers and find the low points by checking its surroundings
# A low point will have numbers larger than it surronding it
for y in range(len(lines)):
    for x in range(len(lines[0])):
        # If position [0][0] exclude checking [y-1][x-1]
        if (x == 0 and y == 0):
            # Check if numbers to right and below are greater than it 
            if (lines[y][x + 1] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If position [y][0] (where y is last index) exclude checking [y+1][x-1]
        elif (x == 0 and y == (len(lines) - 1)):
            # Check if numbers to right and above are greater than it
            if(lines[y][x + 1] > lines[y][x] and lines[y - 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If position [0][x] exclude checking [y-1][x+1]
        elif (x == (len(lines[0]) - 1) and y == 0):
            # Check if numbers to left and below are greater than it
            if(lines[y][x - 1] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If position [y][x] exclude checking [y+1][x+1]
        elif (x == (len(lines[0]) - 1) and y == (len(lines) - 1)):
            # Check if numbers to left and above are greater than it
            if(lines[y][x - 1] > lines[y][x] and lines[y - 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If this is the first line check if points right, left, and below are greater than it
        elif (y == 0):
            if(lines[y][x + 1] > lines[y][x] and lines[y][x - 1] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If this is the last line check if points right, left, and above are greater than it
        elif (y == (len(lines) - 1)):
            if(lines[y][x + 1] > lines[y][x] and lines[y][x - 1] > lines[y][x] and lines[y - 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If this is the left most line check if positions right, above, and below are greater than it
        elif(x == 0):
            if(lines[y][x + 1] > lines[y][x] and lines[y - 1][x] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # If this is the right most line check if position left, above and below are greater than it
        elif(x == (len(lines[0]) - 1)):
            if(lines[y][x - 1] > lines[y][x] and lines[y - 1][x] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                lowPoints.append(lines[y][x])
        # Otherwise check if points above, below, left, and right are greater than it 
        else:
            if(lines[y + 1][x] > lines[y][x] and lines[y - 1][x] > lines[y][x] and lines[y][x - 1] > lines[y][x] and lines[y][x + 1] > lines[y][x]):
                lowPoints.append(lines[y][x])
        
print(calculateRiskLevel(lowPoints))

inputFile.close()
