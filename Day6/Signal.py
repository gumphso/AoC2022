packet = []
#PART ONE ANS == 4, PART TWO ANS 14
packetlength = 14
# number of characters processed
charNum = 0
with open("Day6\input6.txt") as f:
    signal = f.readline()
    # read for each character in the line
    for character in signal:
        # increment number count
        charNum += 1
        # if packet is one less than the desired size, append and check
        if (len(packet) == packetlength-1):
            packet.append(character)
            # if the packet length is equal to the length of the set, break
            # Sets have no duplicate elements
            if len(packet) == len(set(packet)):
                break
            else:
                # if there are repeating elements, pop first element and continue
                packet.pop(0)
        else:
            packet.append(character)
    print(charNum)
