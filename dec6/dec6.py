
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def modelDay(fishList):
    newCount = 0
    for i in range(len(fishList)):
        fishList[i] -= 1
        if fishList[i] < 0:
            newCount += 1
            fishList[i] = 6
    newFish = [8 for _ in range(newCount)]
    fishList.extend(newFish)
        

def modelGrowth(fishList, dayCount):
    for _ in range(dayCount):
        modelDay(fishList)

def main():
    fileName = 'input.txt'
    fishList = list(map(lambda x: int(x), readFile(fileName).split(',')))
    modelGrowth(fishList, 80)
    print(f'fishCount = {len(fishList)}') # 395627




if __name__ == '__main__':
    main()