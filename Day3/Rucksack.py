import string
alphabet = list(string.ascii_lowercase)
alphabet[26:26] = list(string.ascii_uppercase)
sumTotal = 0

with open("Day3\input3.txt") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        rucksackSize = len(line.strip())
        middle = int(rucksackSize/2)
        half1 = line[0 : middle]
        half2 = line[middle : rucksackSize]
        ans = [i for i in half2 if i in half1][0]
        sumTotal += alphabet.index(ans) + 1
    print(sumTotal)