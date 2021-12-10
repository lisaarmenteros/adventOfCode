# Advent of Code - Day 10 Problem 2

closingBrackets = {
            "(":")",
            "[":"]",
            "{":"}",
            "<":">"
}
points = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
}
stack = []
scores = []

# Calculate the points for the incomplete line by checking the closing tags it should use 
def calculateScore(stack):
    total = 0
    for i in reversed(range(len(stack))):
        closingBracket = closingBrackets[stack[i]]
        total = (total * 5) + points[closingBracket]
    
    return total

# Open file and read input
inputFile = open ('input/d10_input.txt','r')
lines = list(inputFile.readlines())

# Read through lines and check if it is incomplete or corrupt.
# If the line is corrupt it will be ignored and a score will be calculated for the incomplete line.
for i in range(len(lines)):
    lines[i] = list(lines[i].strip())
    toKeep = True
    for j in range(len(lines[i])):
        if lines[i][j] == ")" and "(" in stack[-1]:
            stack.pop()
        elif lines[i][j] == "]" and "[" in stack[-1]:
            stack.pop()
        elif lines[i][j] == "}" and "{" in stack[-1]:
            stack.pop() 
        elif lines[i][j] == ">" and "<" in stack[-1]:
            stack.pop() 
        elif lines[i][j] == "(" or lines[i][j] == "[" or lines[i][j] == "{" or lines[i][j] == "<":
            stack.append(lines[i][j])
        else:
            # Error, this line is corrupt
            toKeep = False
            break
    
    # Calculate points for incomplete line
    if(toKeep):
        scores.append(calculateScore(stack))
    stack.clear()

# Sort the list of points to get the middle one
scores.sort()
print(scores[int(len(scores)/2)])