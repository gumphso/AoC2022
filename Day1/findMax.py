# number of elves, highest calorie elf, calorie counter, highest calorie amount
elfcount, elfTrack, calorieCount, calorieMax = 0, 0, 0, 0
# array of top 3 calorie counts
topThreearray = [0, 0, 0]
with open('Day1\input.txt') as f:
    while True:
        line = f.readline()
        if line != "\n" and len(line) != 0:
            calorieCount += int(line)
        else:
            # increment amount of elves
            elfcount += 1
            # if elf has most amount of calories, mark his number
            if calorieCount > calorieMax:
                elfTrack = elfcount
            # if new calorie count is higher than the smallest value in the array, replace that value
            if calorieCount > min(topThreearray):
                topThreearray[topThreearray.index(
                    min(topThreearray))] = calorieCount
                calorieMax = topThreearray[topThreearray.index(
                    max(topThreearray))]
            calorieCount = 0
            # read till EOF
            if len(line) == 0:
                break
# Print sums
print("Top Elf is #"+str(elfTrack)+" with "+str(calorieMax) +
      " total calories, sum of top three is "+str(sum(topThreearray)))
