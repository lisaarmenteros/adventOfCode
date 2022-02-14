# Advent of Code - Day 9 Problem 2

# Using backtracking check the points around it. If the numbers around the point do not exit the array of numbers, 
# encounter a 9, or has been visited add one to the size of basin (by returning one + each side checked)
def findBasins(lines, x, y, visitedPoints):
    if(x < 0 or x >= len(lines) or y < 0 or y>= len(lines[0]) or lines[y][x] == 9 or ([x,y]) in visitedPoints):
        return 0
    else:
        visitedPoints.append([x,y])
        above = findBasins(lines, x, y - 1, visitedPoints)
        below = findBasins(lines, x, y + 1, visitedPoints)
        right = findBasins(lines, x + 1, y, visitedPoints)
        left = findBasins(lines, x - 1, y, visitedPoints)
        # Return 1 + above + below + left + right
        return 1 + above + below + right + left

# Open file and read input
inputFile = open ('../input/d9_input.txt','r')
lines = list(inputFile.readlines())

sizeOfBasins = []
visitedPoints = []

# Split line of numbers into their own sublist
for i in range(len(lines)):
    lines[i] = list(map(int, list(lines[i].strip())))

# Run throught the list of numbers and find the low points by checking its surroundings
# A low point will have numbers larger than it surronding it
# Low points are then used for checking the size of basin
for y in range(len(lines)):
    for x in range(len(lines[0])):
        # If position [0][0] exclude checking [y-1][x-1]
        if (x == 0 and y == 0):
            # Check if numbers to right and below are greater than it 
            if (lines[y][x + 1] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If position [y][0] (where y is last index) exclude checking [y+1][x-1]
        elif (x == 0 and y == (len(lines) - 1)):
            # Check if numbers to right and above are greater than it
            if(lines[y][x + 1] > lines[y][x] and lines[y - 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If position [0][x] exclude checking [y-1][x+1]
        elif (x == (len(lines[0]) - 1) and y == 0):
            # Check if numbers to left and below are greater than it
            if(lines[y][x - 1] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If position [y][x] exclude checking [y+1][x+1]
        elif (x == (len(lines[0]) - 1) and y == (len(lines) - 1)):
            # Check if numbers to left and above are greater than it
            if(lines[y][x - 1] > lines[y][x] and lines[y - 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If this is the first line check if points right, left, and below are greater than it
        elif (y == 0):
            if(lines[y][x + 1] > lines[y][x] and lines[y][x - 1] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If this is the last line check if points right, left, and above are greater than it
        elif (y == (len(lines) - 1)):
            if(lines[y][x + 1] > lines[y][x] and lines[y][x - 1] > lines[y][x] and lines[y - 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If this is the left most line check if positions right, above, and below are greater than it
        elif(x == 0):
            if(lines[y][x + 1] > lines[y][x] and lines[y - 1][x] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # If this is the right most line check if position left, above and below are greater than it
        elif(x == (len(lines[0]) - 1)):
            if(lines[y][x - 1] > lines[y][x] and lines[y - 1][x] > lines[y][x] and lines[y + 1][x] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))
        # Otherwise check if points above, below, left, and right are greater than it 
        else:
            if(lines[y + 1][x] > lines[y][x] and lines[y - 1][x] > lines[y][x] and lines[y][x - 1] > lines[y][x] and lines[y][x + 1] > lines[y][x]):
                sizeOfBasins.append(findBasins(lines, x, y, visitedPoints))

# Sort the list so that the three largest numbers can be easily multiplied
sizeOfBasins.sort()
print(sizeOfBasins[-1]*sizeOfBasins[-2]*sizeOfBasins[-3])

inputFile.close()