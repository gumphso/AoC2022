pointTotal = 0
#opponent input, points
gameMatrix = [['A', 1],['B', 2],['C', 3]]

def findPoints(val1, val2):
    temp = [0,0]
    for choice in gameMatrix:
        if val1 in choice:
            if val2 == 'X':
                temp[0] = gameMatrix[(2 + gameMatrix.index(choice)) % 3][1] 
                temp[1] = 0
                #return ((1 + gameMatrix.index(choice)) % 3) 
            if val2 == 'Y':
                temp[0] = gameMatrix[gameMatrix.index(choice)][1] 
                temp[1] = 3
                
                #return gameMatrix.index(choice)
            if val2 == 'Z':
                temp[0] = gameMatrix[(1 + gameMatrix.index(choice)) % 3][1] 
                temp[1] = 6
                
            return temp
                #return ((2 + gameMatrix.index(choice)) % 3)

with open("Day2\input2.txt") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        result = findPoints(line[0],line[2])
        pointTotal = pointTotal + result[0] + result[1]
    print(pointTotal)
            

