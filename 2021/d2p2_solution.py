# Advent of Code - Day 2 Problem 2

inputFile = open ('d2_input.txt','r')

Lines = inputFile.readlines()
depth=0
horzpos=0
aim=0

for i in range (len(Lines)):
    instruction = Lines[i].split()
    if(instruction[0] == "forward"):
        horzpos += int(instruction[1])
        depth += (aim * int(instruction[1]))
    elif (instruction[0] == "down"):
        aim += int(instruction[1])
    elif (instruction[0] == "up"):
        aim -= int(instruction[1])

print(depth * horzpos)

inputFile.close()