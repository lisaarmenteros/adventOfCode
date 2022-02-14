# Advent of Code - Day 14 Problem 1

def checkOccurrences(polymer):
    occurrences = {}
    
    occurrences["B"] = polymer.count("B")
    occurrences["C"] = polymer.count("C")
    occurrences["F"] = polymer.count("F")
    occurrences["H"] = polymer.count("H")
    occurrences["K"] = polymer.count("K")
    occurrences["N"] = polymer.count("N")
    occurrences["O"] = polymer.count("O")
    occurrences["P"] = polymer.count("P")
    occurrences["S"] = polymer.count("S")
    occurrences["V"] = polymer.count("V")

    minOccurrence = min(occurrences, key=occurrences.get)
    maxOccurrence = max(occurrences, key=occurrences.get)

    print(occurrences[maxOccurrence] - occurrences[minOccurrence])

def pairinsertion(polymer, instructions, iterations):
    toBeInserted = {}
    for j in range(iterations):
        for i in range(len(polymer) - 1):
            if polymer[i] + polymer[i + 1] in instructions:
                toBeInserted[i + 1] = instructions[polymer[i] + polymer[i + 1]]
        
        # i is the index at which the letters are to be inserted and toBeInserted[i] is the letter to be inserted at that index
        # The insertions are made in reversed order to keep the insertion indexes unchanged as insertions get done
        for i in reversed(toBeInserted):
            polymer.insert(i, toBeInserted[i])
    
    checkOccurrences(polymer)

def main():
    inputFile = open('../input/d14_input.txt')
    polymer = list(inputFile.readline().strip())
    inputFile.readline() # Skip over new line
    lines = inputFile.readlines()
    instructions = {}

    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(" -> ")
        instructions[lines[i][0]] = lines[i][1] 

    pairinsertion(polymer, instructions, 10)

main()