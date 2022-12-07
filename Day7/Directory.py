# cd dir
# cd ..
# ls
# size file
#[level, name, size, []]
#dirBranches[dirBrancher.index]
#[level, name, size, [[level, name, size, []],[level, name, size, []]]]

deepestDir = [0,None]
dirLevel = 0

class directory:
    def __init__(self, parent=None, name=None):
        self.name = name
        self.size = 0
        self.parent = parent
        self.nesteddir = []
        self.depth = 0

#beginning parent = none, lowest elements nesteddir
#def checkDirectories():

#highest to lowest list


with open("Day7\input7.txt") as f:
    while True:
        line = f.readline()
        # run till EOF
        if len(line) == 0:
            break
        
        if '/' in line:
            currentDir = directory(name="/")
            root = currentDir
        elif '$' in line:
            if line[2:4] == 'cd':
                print("change dir")
                if (currentDir.parent == None):
                        print("hit")
                if line[5:].strip() == '..' and currentDir.parent != None:
                    #can you go above the root?
                    currentDir = currentDir.parent
                    dirLevel-=1
                    
                else:
                    dirLevel+=1
                    for dir in currentDir.nesteddir:
                        print(line[5:])
                        if line[5:].strip() == dir.name:
                            currentDir = dir
                            if (dirLevel)>deepestDir[0]:
                                deepestDir[0] = dirLevel
                                deepestDir[1] = currentDir
                            break
                
            if line[2:4] == 'ls':
                print("list dir")
        elif 'dir' in line:
            name = line[4:].strip()
            print("directory")
            if not any(dir for dir in currentDir.nesteddir if name == dir.name):
                currentDir.nesteddir.append(directory(currentDir, name))
            
        else:
            print("file")
            currentDir.size += int(line.split(' ')[0])
    print(deepestDir)
    print(deepestDir[1].name)

            
        
