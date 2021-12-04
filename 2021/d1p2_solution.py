# Advent of Code - Day 1 Problem 2

inputFile = open ('input/d1_input.txt','r')

Lines = inputFile.readlines()
count = 0

# Iterrate through the lines and count which lines increment from the previous line (in a 3 measurement window)
for i in range (len(Lines)-3):
    if (int(Lines[i]) + int(Lines[i + 1 ]) + int(Lines[i +2])) < (int(Lines[i + 1]) + int(Lines[i + 2]) + int(Lines[i + 3])):
        count+=1

print(count)

inputFile.close()