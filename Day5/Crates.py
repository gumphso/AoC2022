# array to hold crate values
crateArray = []
# array to hold current crane action
commandArray = []

with open("Day5\input5.txt") as f:
    while True:
        line = f.readline()
        # run till EOF
        if len(line) == 0:
            break
        # find and add crate values to array
        if line != None and "[" in line:
            var = 0
            # find the number of crates across
            for char in range((len(line)//4)):
                # if array is smaller than the number of crates across, add new line of crates
                if len(crateArray) < char+1:
                    crateArray.append([])
                # add element of the line to its appropriate stack if its not a space
                if line[var+1] != ' ':
                    crateArray[char].append([line[var+1]])
                # increment to next element
                var += 4
        # find and split commands based on delimiters
        if line != None and "move" in line:
            # set second, fourth, and sixth elements in line to array
            commandArray = line.strip().split(' ')[1:6:2]
            # loop for the amount of times the procedure happens for the arrangement
            # for example, if we move 2 from 1 to 3, we would loop 2 times
            for amount in range(int(commandArray[0])):
                # pop element from the top of the selected stack for the procedure
                temp = crateArray[int(commandArray[1])-1].pop(0)
                # insert element in the destination stack for the procedure
                crateArray[int(commandArray[2])-1].insert(0, temp)
    # print first letter of each stack
    for x in crateArray:
        print(x[0])
