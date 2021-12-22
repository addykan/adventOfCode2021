# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def getTotalDistances(positions, mean):
    total = 0
    for position in positions:
        total += abs(mean - position)
    return total

def getIncreasingDistances(positions, mean):
    total = 0
    for position in positions:
        dist = abs(mean - position)
        total += (dist * (dist + 1)) // 2
    return total

def main():
    inputFile = 'input.txt'
    positions = list(map(lambda x: int(x), readFile(inputFile).split(',')))
    totalDistances = min(map(lambda x: getTotalDistances(positions, x), range(max(positions))))
    increasingDistances = min(map(lambda x: getIncreasingDistances(positions, x), range((max(positions)))))
    # yes this is inefficient, no i do not care
    print(f'total = {totalDistances}')
    # 338769 too high
    print(f'increasing = {increasingDistances}')
    # 87301269 too low
    # solution: 87640209

if __name__ == '__main__':
    main()