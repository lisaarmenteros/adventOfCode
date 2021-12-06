# Advent of Code - Day 6 Problem 1

inputFile = open ('input/d6_input.txt','r')
lines = inputFile.readlines()
lines = lines[0].split(",")


# Cicle through 80 days
for i in range(80):
    for j in range(len(lines)):
        # If number == 0, set it = 6 and append 8 to the end of the list
        if int(lines[j]) == 0:
            lines[j] = 6
            lines.append(8)
        # ElIf number is <=8, set it -= 1
        elif int(lines[j]) <= 8:
            lines[j] = int(lines[j]) - 1

print(len(lines))

inputFile.close()