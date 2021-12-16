# Advent of Code - Day 14 Problem 2

def checkOccurrences(polymerCount):
    occurrences = {}
    firstPolymer = {}
    secondPolymer = {}

    for i in polymerCount:
        if i[0] not in firstPolymer: 
           firstPolymer[i[0]] = 0
        if i[1] not in secondPolymer: 
           secondPolymer[i[1]] = 0
        firstPolymer[i[0]] += polymerCount[i]
        secondPolymer[i[1]] += polymerCount[i]
    
    occurrences.update(firstPolymer)
    occurrences.update(secondPolymer)

    minOccurrence = min(occurrences, key=occurrences.get)
    maxOccurrence = max(occurrences, key=occurrences.get)

    return occurrences[maxOccurrence] - occurrences[minOccurrence]

def pairinsertion(polymer, instructions, iterations):

    # Create a dictionary of the polymers and their count
    polymerCount = {}
    for i in range(len(polymer) - 1):
        if polymer[i] + polymer[i + 1] not in polymerCount: 
            polymerCount[polymer[i] + polymer[i + 1]] = 0
        polymerCount[polymer[i] + polymer[i + 1]] += 1

    # Creates the new polymerCount by creating a new dictionary and apending the values to the existing polymerCount
    for _ in range(iterations):
        newPolymerCount = {}
        for i in polymerCount:
            if i[0] + instructions[i] not in newPolymerCount: 
                newPolymerCount[i[0] + instructions[i]] = 0
            newPolymerCount[i[0] + instructions[i]] += polymerCount[i]
            if instructions[i] + i[1] not in newPolymerCount: 
                newPolymerCount[instructions[i] + i[1]] = 0
            newPolymerCount[instructions[i] + i[1]] += polymerCount[i]
        polymerCount = newPolymerCount

    print(checkOccurrences(polymerCount))


def main():
    inputFile = open('input/d14_input.txt')
    polymer = list(inputFile.readline().strip())
    inputFile.readline() # Skip over new line
    lines = inputFile.readlines()
    instructions = {}

    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(" -> ")
        instructions[lines[i][0]] = lines[i][1] 

    pairinsertion(polymer, instructions, 40)

main()