
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def part1(depthList):
    increasing = 0
    lastVal = depthList[0]
    for i in range(1, len(depthList)):
        if depthList[i] > lastVal:
            increasing += 1
        lastVal = depthList[i]
    return increasing

def part2(depthList):
    increasing = 0
    lastSum = sum(depthList[:3])
    for i in range(1, len(depthList) - 2):
        slidingWindow = depthList[i:i+3]
        slidingSum = sum(slidingWindow)
        assert(len(slidingWindow) == 3)
        if slidingSum > lastSum:
            increasing += 1
        lastSum = slidingSum
    return increasing

def main():
    dataPath = 'data.txt'
    depthList = list(map(lambda x: int(x), readFile(dataPath).splitlines()))
    # depthList = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    part1Sol = part1(depthList)
    print(part1Sol)
    part2Sol = part2(depthList)
    print(part2Sol)
    return 0

if __name__ == '__main__':
    main()