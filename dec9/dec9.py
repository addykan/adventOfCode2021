# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def makeList(s):
    res = []
    for line in s.splitlines():
        row = []
        for c in line:
            row.append(int(c))
        res.append(row)
    return res

def inBounds(L, row, col):
    # return row >= 0 and row < len(L) and col >= 0 and col < len(L[row])
    return 0 <= row < len(L) and 0 <= col < len(L[row])

def findLowPoints(numberList):
    res = []
    for i in range(len(numberList)):
        for j in range(len(numberList[i])):
            center = numberList[i][j]
            # print(center)
            lowPoint = True
            for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow, newCol = i + drow, j + dcol
                if inBounds(numberList, newRow, newCol):
                    if numberList[newRow][newCol] <= center:
                        lowPoint = False
            if lowPoint:
                res.append(center)
    return res

def main():
    inputFile = 'input.txt'
    numberList = makeList(readFile(inputFile))
    print(numberList[0])
    lowPoints = findLowPoints(numberList)
    riskSum = sum(map(lambda x: x + 1, lowPoints))
    print(f'risk sum = {riskSum}')
    # 7034 too high
    # Solution: 558

if __name__ == '__main__':
    main()
