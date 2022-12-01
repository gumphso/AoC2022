
elfcount, elfTrack, calorieCount, calorieMax = 0,0,0,0

with open('Day1\input.txt') as f:
    for line in f:
        if line != "\n":
            calorieCount += int(line)
        else:
            elfcount += 1
            if calorieCount > calorieMax:
                elfTrack = elfcount
                calorieMax = calorieCount
            calorieCount = 0

print("Elf #"+str(elfTrack)+" with "+str(calorieMax)+" total calories")



