pointTotal = 0
#opponent input, player input, points, winIndex 
gameMatrix = [['A','X', 1 , 2],['B','Y', 2, 0],['C','Z', 3, 1]]

def findChoice(val1, val2):
    temp = [0,0,0,0]
    for choice in gameMatrix:
        #opponent
        if val1 in choice:
            temp[0] = choice[3]
            temp[3] = gameMatrix.index(choice)
        #player
        if val2 in choice:
            temp[1] = choice[3]
            temp[2] = choice[2]
    return temp

with open("Day2\input2.txt") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        result = findChoice(line[0],line[2])
        pointTotal += result[2]
        if result[0] == result[1]:
            pointTotal += 3
        if result[1] == result[3]:
            pointTotal += 6
    print(pointTotal)
            

