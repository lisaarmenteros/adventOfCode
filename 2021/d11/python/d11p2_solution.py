# Advent of Code - Day 11 Problem 2

# Every enery level or step has the following take place
# 1) First, the energy level of each octopus increases by 1.
# 2) Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, 
# including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes.
# This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at 
# most once per step.)
# 3) Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

inputFile = open('../input/d11_input.txt','r')
octopus = list(inputFile.readlines())

for i in range(len(octopus)):
    octopus[i] = list(map(int,octopus[i].strip()))

def flash(octopus, x, y):
    if x < 0 or x >= len(octopus) or y < 0 or y >= len(octopus[0]) or octopus[y][x] > 9:
        return
    
    octopus[y][x] += 1

    if octopus[y][x] > 9:
        flash(octopus, x, y - 1) # Above
        flash(octopus, x, y + 1) # Below
        flash(octopus, x - 1, y) # Left
        flash(octopus, x + 1, y) # Right
        flash(octopus, x + 1, y - 1) # UpperRight
        flash(octopus, x - 1, y - 1) # UpperLeft
        flash(octopus, x + 1, y + 1) # LowerRight
        flash(octopus, x - 1, y + 1) # LowerLeft
    
timesFlashed = 0
iterations = 1

# Continue until all the octopus have flashed at the same time
while True:
    # Iterate through the graph of octopus
    for y in range(len(octopus)):
        for x in range(len(octopus[y])):
            # Increments octopus[y][x] by one and flashes its surroundings 
            flash(octopus, x, y)

    # Check anything with a number greater than 9 (flashed) and set it to zero. Increment timesFlashed
    for y in range(len(octopus)):
        for x in range(len(octopus[y])):
            if octopus[y][x] > 9:
                octopus[y][x] = 0
                timesFlashed += 1
    
    # Check if all flashed at same time. If so, print the iteration we are on
    if(timesFlashed == 100):
        print(iterations)
        break

    timesFlashed = 0
    iterations += 1