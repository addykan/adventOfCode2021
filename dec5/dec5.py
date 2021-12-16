
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)


# def findMaxVal(pathStrings):
#     maxVal = -1
#     for line in pathStrings:
#         start, end = line.split('->')
#         (x1, y1), (x2, y2) = start.split(','), end.split(',')
#         for val in map(lambda x: int(x), (x1, y1, x2, y2)):
#             if val > maxVal:
#                 maxVal = val
#     return maxVal

class VentLine:
    def __init__(self, pathString):
        start, end = pathString.split('->')
        (x1, y1), (x2, y2) = start.split(','), end.split(',')
        self.x1, self.y1, self.x2, self.y2 = list(map(lambda x: int(x), [x1, y1, x2, y2]))
    
    def __repr__(self):
        return f'{self.x1},{self.y1} -> {self.x2},{self.y2}'

def addRow(ventList, line):
    start = min(line.x1, line.x2)
    end = max(line.x1, line.x2)
    print(f'start = {start}, end = {end}')
    for col in range(start, end+1):
        print('incrementing')
        ventList[line.x1][col] += 1
        print(f'ventList[line.x1 = {line.x1}][col = {col}] = {ventList[line.x1][col]}')


def addCol(ventList, line):
    start = min(line.y1, line.y2)
    end = max(line.y1, line.y2)
    for row in range(start, end + 1):
        print('also incrementing')
        ventList[row][line.y1] += 1
        print(f'ventList[row = {row}][line.y1 = {line.y1}] = {ventList[row][line.y1]}')


def addLine(ventList, line):
    if line.x1 == line.x2:
        print(line)
        addCol(ventList, line)
    elif line.y1 == line.y2:
        print(line)
        addRow(ventList, line)

def addLines(ventList, lineList):
    for line in lineList:
        addLine(ventList, line)

def countIntersections(ventList):
    total = 0
    # print(ventList)
    for row in ventList:
        for elem in row:
            if elem >= 2:
                total += 1
    return total

def main():
    fileName = 'input.txt'
    pathStrings = readFile(fileName).splitlines()
    maxVal = 1000
    ventList = [[0] * maxVal for _ in range(maxVal)]
    lineList = list(map(lambda s: VentLine(s), pathStrings))
    addLines(ventList, lineList)
    intersectionCount = countIntersections(ventList)
    print(f'Intersection count: {intersectionCount}') # 7656
    


if __name__ == '__main__':
    main()