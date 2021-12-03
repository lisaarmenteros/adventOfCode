# Advent of Code - Day 3 Problem 1
# Extremely brute-force solution. May work on something more clean

inputFile = open ('input/d3_input.txt','r')

Lines = inputFile.readlines()

length = len(list(Lines[0]))
gamma = 0
epsilon=0

for i in range(length - 1):
    numzeros=0
    numones=0
    for j in range(len(Lines)):
        binary = list(Lines[j])
        if binary[i] == "1":
            numones+=1
        if binary[i] == "0":
            numzeros += 1 
    if numones > numzeros:
        gamma += (2 ** (length -2 - i))
    if numones < numzeros:
        epsilon += (2 ** (length -2 - i))

print(gamma * epsilon)

inputFile.close()