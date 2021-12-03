import math

# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def getStats(strings):
    mostCommon = -1
    mostCount = -1
    leastCommon = -1
    leastCount = math.inf
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


def main():
    filePath = 'input.txt'
    strings = readFile(filePath).splitlines()
    getStats(strings)
    return 0

if __name__ == '__main__':
    main()