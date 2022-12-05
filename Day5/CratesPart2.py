crateArray = []
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
            # cut a slice off the top of the first stack for the procedure
            temp = crateArray[int(commandArray[1])-1][0:int(commandArray[0])]
            # delete the portion of the array sliced
            del crateArray[int(commandArray[1])-1][0:int(commandArray[0])]
            # add the slice at the beginning (top) of the destination stack for the procedure
            crateArray[int(commandArray[2])-1] = temp + \
                crateArray[int(commandArray[2])-1]
    for x in crateArray:
        print(x[0])
