pointTotal = 0
# order matters, elements on right beat element on left if array loops
# for example A (rock) beats C (scissors), and B (Paper) beats A
# [opponent input, points]
gameMatrix = [['A', 1], ['B', 2], ['C', 3]]


def findPoints(val1, val2):
    temp = [0, 0]
    for choice in gameMatrix:
        if val1 in choice:
            # Want to end in loss
            if val2 == 'X':
                temp[0] = gameMatrix[(2 + gameMatrix.index(choice)) % 3][1]
                temp[1] = 0
            # want to end in draw
            if val2 == 'Y':
                temp[0] = gameMatrix[gameMatrix.index(choice)][1]
                temp[1] = 3
            # want to end in win
            if val2 == 'Z':
                temp[0] = gameMatrix[(1 + gameMatrix.index(choice)) % 3][1]
                temp[1] = 6

            return temp


with open("Day2\input2.txt") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        result = findPoints(line[0], line[2])
        # add points for playing choice and game outcome
        pointTotal = pointTotal + result[0] + result[1]
    print(pointTotal)
