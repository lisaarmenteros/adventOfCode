# Advent of Code - Day 8 Problem 1

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

inputFile = open ('input/d8_input.txt','r')
lines = inputFile.readlines()

numTimes = 0

# Read file and gather the number of 1, 4, 7, or 8s
for i in range(len(lines)):
    lines[i] = lines[i].strip().split(" | ")
    outputValues = lines[i][1].split()
    for j in range(len(outputValues)):
        if(len(outputValues[j]) == 2 or len(outputValues[j]) == 4 or len(outputValues[j]) == 3 or len(outputValues[j]) == 7):
            numTimes += 1

print("Num times:", numTimes)

inputFile.close()