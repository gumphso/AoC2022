
elfcount, elfTrack, calorieCount, calorieMax = 0,0,0,0
topThreearray = [0,0,0]
with open('Day1\input.txt') as f:
    while True:
        line = f.readline()
        if line != "\n" and len(line) != 0:
            calorieCount += int(line)
        else:
            elfcount += 1
            if calorieCount > calorieMax:
                elfTrack = elfcount
            if calorieCount > min(topThreearray):
                topThreearray[topThreearray.index(min(topThreearray))] = calorieCount
                calorieMax = topThreearray[topThreearray.index(max(topThreearray))]
            calorieCount = 0
            if len(line) == 0:
                break

print("Top Elf is #"+str(elfTrack)+" with "+str(calorieMax)+" total calories, sum of top three is "+str(sum(topThreearray)))



