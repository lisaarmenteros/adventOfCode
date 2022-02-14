# Advent of Code - Day 8 Problem 2

#  0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# Note: Input will not match sequence above, but this is a good example of sequences and their matching numbers
# Note: By default 1, 4, 7, and 8 has unique number of segments

# Takes in output sequence and list of numbers containing their matching enabled segments to calculate the output (in digits)
def calculateOutput(numbers, outputValues):
    total = 0
    for i in range(len(outputValues)):
        for j in range(len(numbers)):
            if len(outputValues[i]) == len(numbers[j]) and len(set(outputValues[i]) & set(numbers[j])) == len(outputValues[i]):
                total += int(j) * (10 ** (len(outputValues) - i -1))
                break
    
    return total
 
inputFile = open ('../input/d8_input.txt','r')
lines = inputFile.readlines()
output = []
numbers = {}

# Read through file and seperate input from output. Input is used to deduct which number each sequence of enabled segments is
# Output is then calculated knowing now which numbers match up with enabled segments
for j in range(len(lines)):
    inputValues = lines[j].strip().split(" | ")[0].split()
    outputValues = lines[j].strip().split(" | ")[1].split()

    # Read through input values and get 1, 4, 7, and 8 since each of these has a unique number of segments to be enabled
    for i in range(len(inputValues)):
        # The number is a 1: Enables 2 segment 
        if(len(inputValues[i]) == 2): 
            numbers[1] = inputValues[i]
        # The number is a 4: Enables 4 segments
        elif(len(inputValues[i]) == 4): 
            numbers[4] = inputValues[i]
        # The number is a 7: Enables 3 segments
        elif(len(inputValues[i]) == 3): 
            numbers[7] = inputValues[i] 
        # The number is an 8: Enables 7 segments
        elif(len(inputValues[i]) == 7): 
            numbers[8] = inputValues[i]

    # Gather remaining numbers by using the numbers we already know (1, 4, 7, 8)
    for i in range(len(inputValues)):
        # The number is a zero: Enables 6 segments, contains the same two segments as number 1, contains three of four segments of number 4
        if(len(inputValues[i]) == 6 and len(set(inputValues[i]) & set(numbers[1])) == 2 and len(set(inputValues[i]) & set(numbers[4])) == 3): 
            numbers[0] = inputValues[i] 
        # The number is a nine: Enables 6 segments, contains the same four segments as number 4
        elif(len(inputValues[i]) == 6 and len(set(inputValues[i]) & set(numbers[4])) == 4): 
            numbers[9] = inputValues[i]
        # The number is a six: Enables 6 segments, does not fit the characteristics of number 0 & number 9 (which both also enable 6 segments)
        elif(len(inputValues[i]) == 6): 
            numbers[6] = inputValues[i]
        # The number is a three: Enables 5 segments, contains the same two segments as number 1
        elif(len(inputValues[i]) == 5 and len(set(inputValues[i]) & set(numbers[1])) == 2): 
            numbers[3] = inputValues[i]
        # The number is a five: Enables 5 segments, contains three of four segments of number 4
        elif(len(inputValues[i]) == 5 and len(set(inputValues[i]) & set(numbers[4])) == 3): 
            numbers[5] = inputValues[i]
        # The number is a two: Enables 5 segments, contains two of four segments of number 4
        elif (len(inputValues[i]) == 5 and len(set(inputValues[i]) & set(numbers[4])) == 2): 
            numbers[2] = inputValues[i]
    
    # Adds the calculated output into the list of outputs
    output.append(calculateOutput(numbers, outputValues)) 

# Add up all outputs
totalOutput = 0
for i in range(len(output)):
    totalOutput += output[i]
print(totalOutput)

inputFile.close()