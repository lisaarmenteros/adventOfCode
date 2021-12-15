# Advent of Code - Day 13 Problem 2

# x = coordinates[i][0]
# y = coordinates[i][1]
def foldAlongX(coordinates, foldingLine):
    toBeDeleted = []
    toBeAdded = []

    for i in range(len(coordinates)):
        if coordinates[i][0] > foldingLine:
            difference = abs(coordinates[i][0] - foldingLine)
            toBeAdded.append([foldingLine - difference, coordinates[i][1]])
            toBeDeleted.append(i)
                

    # Delete indexes in reverse order to keep indexes consistant 
    # (If deleting from smallest index to largest the second half would shift to left)
    for i in reversed(range(len(toBeDeleted))):
        coordinates.pop(toBeDeleted[i])

    # Add indexes
    for i in range(len(toBeAdded)):
        if toBeAdded[i] not in coordinates:
            coordinates.append(toBeAdded[i])
            

def foldAlongY(coordinates, foldingLine):
    toBeDeleted = []
    toBeAdded = []

    for i in range(len(coordinates)):
        if coordinates[i][1] > foldingLine:
            difference = abs(coordinates[i][1] - foldingLine)
            toBeAdded.append([coordinates[i][0], foldingLine - difference])
            toBeDeleted.append(i)
                

    # Delete indexes in reverse order to keep indexes consistant 
    # (If deleting from smallest index to largest the second half would shift to left)
    for i in reversed(range(len(toBeDeleted))):
        coordinates.pop(toBeDeleted[i])

    # Add indexes
    for i in range(len(toBeAdded)):
        if toBeAdded[i] not in coordinates:
            coordinates.append(toBeAdded[i])

# foldingInstructions[instructionNumber][0] = axis
# foldingInstructions[instructionNumber][1] = number 
def getFoldingInstruction(foldingInstructions, index, lines):
    j = 0
    for i in range (index, len(lines)):
        lines[i] = lines[i].strip().split("=")
        lines[i][0] = lines[i][0].split(" ")[-1]
        
        foldingInstructions[j] = lines[i]
        j += 1

def printCode(coordinates):
    largestX = 0
    largestY = 0
    #Find largest x coordinate and largest y cooradinate to determine the size of the final paper
    for i in range(len(coordinates)):
        if coordinates[i][0] > largestX:
            largestX = coordinates[i][0]
        if coordinates[i][1] > largestY:
            largestY = coordinates[i][1]
    
    # Create paper with empty dots
    paper = ["."] * (largestY + 1)

    for i in range(len(paper)):
        paper[i] = ["."] * (largestX + 1)

    # Go through cooardinates and plot them
    for i in range(len(coordinates)):
        paper[coordinates[i][1]][coordinates[i][0]] = "#"
    
    for i in range(len(paper)):
        print(paper[i])
    

def main():
    inputFile = open('input/d13_input.txt')
    lines = list(inputFile.readlines())

    foldingInstructions = {}
    coordinates = []

    for i in range(len(lines)):
        if len(lines[i]) == 1:
            getFoldingInstruction(foldingInstructions, i + 1, lines)
            break
        lines[i] = lines[i].strip().split(",")
        coordinates.append([int(lines[i][0]),int(lines[i][1])])
    

    # If instruction is to fold from y axis, the y coordinates below this line are subbed from the 
    # distance from this line and added this many positions above the line
    for i in range(len(foldingInstructions)):
        if foldingInstructions[i][0] == "x":
            foldAlongX(coordinates, int(foldingInstructions[i][1]))
        else:
            foldAlongY(coordinates, int(foldingInstructions[i][1]))
    
    printCode(coordinates)

main()