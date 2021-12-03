# Advent of Code - Day 3 Problem 2

inputFile = open ('input/d3_input.txt','r')

listOfBinary = inputFile.readlines()
listOfBinary2 = listOfBinary.copy()

lengthofBinary = len(list(listOfBinary[0])) - 1
emptylist = [None] * lengthofBinary

# Function which takes in a list making up binary list and converts it into an int in decimal form
def convertToDecimal(binaryNumList):
    decimal = 0
    for i in range(lengthofBinary):
        decimal += (int(binaryNumList[i]) * (2 ** (lengthofBinary -1 - i)))
    return decimal
    
# Function to remove binary number from list if it contains a zero in the indicated index
def removeZeros(listOfBinary, index):
    for i in range(len(listOfBinary)):
        if list(listOfBinary[i])[index] == "0":
            del listOfBinary[i]
            listOfBinary.insert(0,emptylist) # Adding empty item equal in size to not disrupt list/array size
    return listOfBinary

# Function to remove binary number from list if it contains a one in the indicated index
def removeOnes(listOfBinary, index):
    for i in range(len(listOfBinary)):
        if list(listOfBinary[i])[index] == "1":
            del listOfBinary[i]
            listOfBinary.insert(0,emptylist) # Adding empty item equal in size to not disrupt list/array size
    return listOfBinary


# Calculate Oxygen 
for i in range(lengthofBinary):
    numzeros=0
    numones=0
    for j in range(len(listOfBinary)): 
            binary = list(listOfBinary[j])
            if binary[i] == "1":
                numones+=1
            if binary[i] == "0":
                numzeros += 1 
    if listOfBinary[-2] == emptylist: # Break early if there is only one number left
            break
    if numones > numzeros:
        listOfBinary = removeZeros(listOfBinary, i)
    elif numones < numzeros:
        listOfBinary = removeOnes(listOfBinary, i)
    elif numones == numzeros:
        listOfBinary = removeZeros(listOfBinary, i)

oxygenGenerator = convertToDecimal(list(listOfBinary[-1]))

# Calculate Carbon
for i in range(lengthofBinary):
    numzeros=0
    numones=0
    for j in range(len(listOfBinary2)):
        binary = list(listOfBinary2[j])
        if binary[i] == "1":
            numones+=1
        if binary[i] == "0":
            numzeros += 1 
    if listOfBinary2[-2] == emptylist: # Break early if there is only one number left
            break
    if numones > numzeros:
        listOfBinary2 = removeOnes(listOfBinary2, i)
    elif numones < numzeros:
        listOfBinary2 = removeZeros(listOfBinary2, i)
    elif numones == numzeros:
        listOfBinary2 = removeOnes(listOfBinary2, i)

carbonScrubber = convertToDecimal(list(listOfBinary2[-1]))

print(oxygenGenerator * carbonScrubber)

inputFile.close() 