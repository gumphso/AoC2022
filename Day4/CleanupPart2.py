import re
containCount = 0

with open("Day4\input4.txt") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        IDs = re.split(r',|-', line.strip())
        if IDs[0] == IDs[1]:
            firstID = [int(IDs[0])]
        else:
            firstID = [*range(int(IDs[0]), int(IDs[1])+1)]
        if IDs[2] == IDs[3]:
            secondID = [int(IDs[2])]
        else:
            secondID = [*range(int(IDs[2]), int(IDs[3])+1)]
        check = [elem for elem in firstID if elem in secondID]
        if check:
            containCount += 1

    print(containCount)