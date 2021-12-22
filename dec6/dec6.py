import copy 

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

def quickModelDay(fishDict):
    newEight = fishDict.get(0, 0)
    # for key in fishDict:
    #     fishDict[key] = fishDict.get(key + 1, 0)
    for i in range(9):
        fishDict[i] = fishDict.get(i + 1, 0)
    fishDict[8] = newEight
    fishDict[6] += newEight

def quickModelGrowth(fishList, dayCount):
    fishDict = dict()
    for fish in fishList:
        fishDict[fish] = fishDict.get(fish, 0) + 1
    for day in range(dayCount):
        quickModelDay(fishDict)
    res = 0
    print(sorted(fishDict.keys()))
    for key in fishDict:
        res += fishDict[key]
    return res

def main():
    fileName = 'input.txt'
    fishList = list(map(lambda x: int(x), readFile(fileName).split(',')))
    secondFishList = copy.deepcopy(fishList)
    modelGrowth(fishList, 80)
    dictModelCount = quickModelGrowth(secondFishList, 256)
    print(f'fishCount = {len(fishList)}') # 395627
    print(f'256 day fishCount = {dictModelCount}')




if __name__ == '__main__':
    main()