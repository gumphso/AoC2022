import string
alphabet = list(string.ascii_lowercase)
alphabet[26:26] = list(string.ascii_uppercase)
groupMember1 = []
groupMember2 = []
groupMember3 = []


sumTotal = 0

with open("Day3\input3.txt") as f:
    lines = f.readlines()
    for x in range(0,len(lines), 3):
        
        groupMember1 = lines[x].strip()
        groupMember2 = lines[x+1].strip()
        groupMember3 = lines[x+2].strip()
        ans = [i for i in groupMember1 if i in groupMember2 and i in groupMember3][0]
        sumTotal += alphabet.index(ans) + 1
    print(sumTotal)