# Advent of Code - Day 2 Problem 1

inputFile = open ('d2_input.txt','r')

Lines = inputFile.readlines()
depth=0
horzpos=0



for i in range (len(Lines)):
    instruction = Lines[i].split()
    if(instruction[0] == "forward"):
        horzpos += int(instruction[1])
        print("Moving forward!")
        print("horpos:", horzpos)
    elif (instruction[0] == "down"):
        depth += int(instruction[1])
        print("Moving down!")
        print("depth:", depth)
    elif (instruction[0] == "up"):
        depth -= int(instruction[1])
        print("Moving up!")
        print("depth:", depth)

print(depth * horzpos)

inputFile.close()