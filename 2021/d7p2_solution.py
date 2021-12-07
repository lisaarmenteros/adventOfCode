# Advent of Code - Day 7 Problem 2

# Read input 
inputFile = open ('input/d7_input.txt','r')
lines = inputFile.readlines()
lines = list(map(int, lines[0].split(",")))

# Calculates the fuel cost by taking that array of fish distances and number to calculate distance from
def calculateFuel(lines, cheapest):
    fuel = 0
    total = 0
    for i in range(len(lines)):
        difference =  abs(cheapest - lines[i]) 
        for j in range(difference + 1):
            total += j
        fuel += total
        total = 0
    return fuel

# Sort input
lines.sort()

# Find the average of the fish distances for the optimized fuel usage
sum = 0
for i in range(len(lines)):
    sum += lines[i]
cheapestNum = int(sum / len(lines))
total = calculateFuel(lines, cheapestNum)
total2 = calculateFuel(lines, cheapestNum + 1) # Account for if the number rounded up is more efficient

if total < total2:
    print(total)
else:
    print(total2)

inputFile.close()