import re
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
        # check if any element in the first array overlap the second, if none then neither overlap
        check = [elem for elem in firstID if elem in secondID]
        # if a overlap was found, increment
        if check:
            containCount += 1

    print(containCount)
