
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def main():
    dataPath = 'data.txt'
    depthList = list(map(lambda x: int(x), readFile(dataPath).splitlines()))
    # depthList = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    increasing = 0
    lastVal = depthList[0]
    for i in range(1, len(depthList)):
        if depthList[i] > lastVal:
            increasing += 1
        lastVal = depthList[i]
    print(increasing)
    return 0

if __name__ == '__main__':
    main()