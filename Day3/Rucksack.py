import string
# String of all upper and lowercase alphabet characters
alphabet = list(string.ascii_lowercase)
alphabet += list(string.ascii_uppercase)
# sum of item priorities
sumTotal = 0

with open("Day3\input3.txt") as f:
    while True:
        line = f.readline()
        # run till EOF
        if len(line) == 0:
            break
        # get size of bag based on line length
        rucksackSize = len(line.strip())
        # break bag into two separate arrays
        middle = int(rucksackSize/2)
        half1 = line[0: middle]
        half2 = line[middle: rucksackSize]
        # find the letter which is present in first and second half
        ans = [i for i in half2 if i in half1][0]
        # sum priority based on the letters index plus one
        sumTotal += alphabet.index(ans) + 1
    print(sumTotal)
