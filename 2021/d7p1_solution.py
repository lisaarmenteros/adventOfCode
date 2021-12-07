# Advent of Code - Day 7 Problem 1

# Read input 
inputFile = open ('input/d7_input.txt','r')
lines = inputFile.readlines()
lines = list(map(int, lines[0].split(",")))


def calculateFuel(list, middle):
    fuel = 0
    for i in range(len(list)):
        fuel += abs(middle - list[i])
    return fuel

# Sort input
lines.sort()

# Get two middle numbers in case the number is even and check which provides a cheaper fuel result
middle = lines[int(len(lines)/2)]
middle2 = lines[int((len(lines)/2)) - 1]

total = calculateFuel(lines, middle)
total2 = calculateFuel(lines, middle2)

if total < total2:
    print(total)
else:
    print(total2)
