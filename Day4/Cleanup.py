import re
# number of sections that go into each other
containCount = 0

with open("Day4\input4.txt") as f:
    while True:
        line = f.readline()
        # read till EOF
        if len(line) == 0:
            break
        # split numbers on delimiters and remove newlines
        IDs = re.split(r',|-', line.strip())
        # if both numbers in the first range are equal, set first ID to single item array
        if IDs[0] == IDs[1]:
            firstID = [int(IDs[0])]
        else:
            # set first ID to range of numbers from the first number to the second, unpacking the range
            firstID = [*range(int(IDs[0]), int(IDs[1])+1)]
        if IDs[2] == IDs[3]:
            # if both numbers in the second range are equal, set second ID to single item array
            secondID = [int(IDs[2])]
        else:
            # set second ID to range of numbers from the first number to the second, unpacking the range
            secondID = [*range(int(IDs[2]), int(IDs[3])+1)]
        # check if all elements in first array fit in the second, and all elements in second array fit in the first
        oneintwo = all(elem in firstID for elem in secondID)
        twoinone = all(elem in secondID for elem in firstID)
        # if they fit, increment sum
        if oneintwo or twoinone:
            containCount += 1

    print(containCount)
