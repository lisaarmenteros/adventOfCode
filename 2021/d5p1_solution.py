# Advent of Code - Day 5 Problem 1

inputFile = open ('input/d5_input.txt','r')
lines = inputFile.readlines()

coordinates = []
overlappingLines = {}
counter = 0

# Loop through the lines assigning coordinates and checking if they make up a stright line (x1=x2 or y1=y2)
for i in range(len(lines)):
    coordinates = lines[i].strip().split(" -> ")
    coordinates[0] = coordinates[0].split(",")
    coordinates[1] = coordinates[1].split(",")

    # If the x coordinates are equal (x1 = x2)
    # ex: 2,6 -> 2,9
    if coordinates[0][0] == coordinates[1][0]: 
        # Checks which of the y coordinates is larger to modify range
        if int(coordinates[0][1]) < int(coordinates[1][1]):
            # Check if the range of y coordinates exist already in dictionary, if not, add it. If, so increment the counter
            for j in range(int(coordinates[0][1]), int(coordinates[1][1]) + 1):
                if (int(coordinates[0][0]),j) in overlappingLines:
                    overlappingLines[int(coordinates[0][0]),j] += 1
                else:
                    overlappingLines[int(coordinates[0][0]),j] = 1
        elif int(coordinates[0][1]) > int(coordinates[1][1]):  
            # Check if the range of y coordinates exist already in dictionary, if not, add it. If, so increment the counter
            for j in range(int(coordinates[1][1]), int(coordinates[0][1]) + 1):
                if (int(coordinates[0][0]),j) in overlappingLines:
                    overlappingLines[int(coordinates[0][0]),j] += 1
                else:
                    overlappingLines[int(coordinates[0][0]),j] = 1
            
    # If y coordinates are equal (y1 = y2)
    # ex: 6,2 -> 9,2
    elif coordinates[0][1] == coordinates[1][1]: 
        # Checks which of the x coordinates is larger to modify range
        if int(coordinates[0][0]) < int(coordinates[1][0]):
            # Check if the range of x coordinates exist already in dictionary, if not, add it. If, so increment the counter
            for j in range(int(coordinates[0][0]), int(coordinates[1][0]) + 1):
                if (j, int(coordinates[0][1])) in overlappingLines:
                    overlappingLines[j, int(coordinates[0][1])] += 1
                else:
                    overlappingLines[j, int(coordinates[0][1])] = 1
        elif int(coordinates[0][0]) > int(coordinates[1][0]): 
            for j in range(int(coordinates[1][0]), int(coordinates[0][0]) + 1):
                if (j, int(coordinates[0][1])) in overlappingLines:
                    overlappingLines[j, int(coordinates[0][1])] += 1
                else:
                    overlappingLines[j, int(coordinates[0][1])] = 1

# Count how many lines overlap more 
for i in overlappingLines:
    if overlappingLines[i] >= 2:
        counter += 1

print(counter)

inputFile.close()