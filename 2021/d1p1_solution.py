# Advent of Code - Day 1 Problem 1

inputFile = open ('d1p1_input.txt','r')

Lines = inputFile.readlines()
count = 0
numlines=0

# Count the number of lines in file 
for line in Lines:
    numlines+=1

# Iterrate through the lines and count which lines increment from the previous line
for i in range (numlines-1):
    if int(Lines[i]) < int(Lines[i + 1]):
        count+=1

print(count)

inputFile.close()