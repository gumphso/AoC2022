import string
alphabet = list(string.ascii_lowercase)
alphabet += list(string.ascii_uppercase)
# 3 arrays for each elf member in the group
groupMember1 = []
groupMember2 = []
groupMember3 = []

sumTotal = 0

with open("Day3\input3.txt") as f:
    lines = f.readlines()
    # Advance through the lines in steps of 3
    for x in range(0, len(lines), 3):

        # assign each of the 3 lines to each of the 3 elves
        groupMember1 = lines[x].strip()
        groupMember2 = lines[x+1].strip()
        groupMember3 = lines[x+2].strip()
        # for each element in the first memebers bag, check to see if it exists in both of the other members bags
        ans = [i for i in groupMember1 if i in groupMember2 and i in groupMember3][0]
        # sum priority based on the letters index plus one
        sumTotal += alphabet.index(ans) + 1
    print(sumTotal)
