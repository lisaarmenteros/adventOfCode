# Advent of Code - Day 13 Problem 1

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
            
    
    print("At the end of folding on line", foldingLine,"the length of coordinates is", len(coordinates))


# foldingInstructions[instructionNumber][0] = axis
# foldingInstructions[instructionNumber][1] = number 
def getFoldingInstruction(foldingInstructions, index, lines):
    j = 0
    for i in range (index, len(lines)):
        lines[i] = lines[i].strip().split("=")
        lines[i][0] = lines[i][0].split(" ")[-1]
        
        foldingInstructions[j] = lines[i]
        j += 1
    

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
    foldAlongX(coordinates, int(foldingInstructions[0][1]))

main()