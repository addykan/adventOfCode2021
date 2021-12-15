import math

# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def getStats(strings):
    strLen = len(strings[0])
    oneCount = [0] * strLen
    for binary in strings:
        for i in range(strLen):
            if binary[i] == '1':
                oneCount[i] += 1
    gammaStr = ''
    epsilonStr = ''
    for one in oneCount:
        if one >= len(strings) // 2:
            gammaStr += '1'
            epsilonStr += '0'
        else:
            gammaStr += '0'
            epsilonStr += '1'
    print(epsilonStr, gammaStr)
    gamma = int(gammaStr, base=2)
    epsilon = int(epsilonStr, base=2)
    print(f'gamma = {gamma}, epsilon = {epsilon}, power consumption = {gamma * epsilon}')

def getStringList(strings, i):
    oneStrings, zeroStrings = [], []
    for string in strings:
        if string[i] == '1':
            oneStrings.append(string)
        else:
            zeroStrings.append(string)
    return oneStrings, zeroStrings

def getStatsPart2(strings):
    possibleVals = [string for string in strings]
    oxygenList = []
    co2List = []
    i = 0
    while len(possibleVals) > 1 and i < len(strings[0]):
        oneStrings, zeroStrings = getStringList(strings, i)
        if len(oneStrings) >= len(zeroStrings):
            possibleVals = oneStrings
        else:
            possibleVals = zeroStrings
        i += 1
    oxygen = int(possibleVals[0], base=2)
    possibleVals = [string for string in strings]
    i = 0
    while len(possibleVals) > 1 and i < len(strings[0]):
        oneStrings, zeroStrings = getStringList(strings, i)
        if len(oneString) >= len(zeroStrings):
            possible

def main():
    filePath = 'input.txt'
    strings = readFile(filePath).splitlines()
    getStats(strings)
    return 0

if __name__ == '__main__':
    main()