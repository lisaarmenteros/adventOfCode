# Advent of Code - Day 10 Problem 1

points = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
}
stack = []
totalPoints = 0

# Open file and read input
inputFile = open ('input/d10_input.txt','r')
lines = list(inputFile.readlines())

# Read through lines and check if it is incomplete or corrupt.
# If the line is incomplete it will be ignored and a score will be calculated for the corrupt line based on the 
# bracket which caused the corruption.
for i in range(len(lines)):
    lines[i] = list(lines[i].strip())

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
            totalPoints += points[lines[i][j]]
            break
        
    stack.clear()

print(totalPoints)