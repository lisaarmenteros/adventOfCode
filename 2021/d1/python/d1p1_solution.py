# Advent of Code - Day 1 Problem 1

inputFile = open ('../input/d1_input.txt','r')

Lines = inputFile.readlines()
count = 0

# Iterrate through the lines and count which lines increment from the previous line
for i in range (len(Lines)-1):
    if int(Lines[i]) < int(Lines[i + 1]):
        count+=1

print(count)

inputFile.close()