# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def isCorrupted(line):
    parenStack = 0 # ()
    bracketStack = 0 # []
    braceStack = 0 # {}
    seqStack = 0 # <>
    for char in line:
        match char:
            case '(':
                parenStack += 1
            case '[':
                bracketStack += 1
            case '{':
                braceStack += 1
            case '<':
                seqStack += 1
            case ')':
                parenStack -= 1
            case ']':
                bracketStack -= 1
            case '}':
                braceStack -= 1
            case '>':
                seqStack -= 1
    stackList = [parenStack, bracketStack, braceStack, seqStack]
    # positives = negatives = False
    for i in stackList:
        if i < 0:
            return True
    return False

def findCorruptedLines(lines):
    res = []
    for line in lines:
        if isCorrupted(line):
            res.append(line)
    return res

def findIllegalCharInLine(line):
    parenStack = 0 # ()
    bracketStack = 0 # []
    braceStack = 0 # {}
    seqStack = 0 # <>
    for char in line:
        match char:
            case '(':
                parenStack += 1
            case '[':
                bracketStack += 1
            case '{':
                braceStack += 1
            case '<':
                seqStack += 1
            case ')':
                parenStack -= 1
            case ']':
                bracketStack -= 1
            case '}':
                braceStack -= 1
            case '>':
                seqStack -= 1
        for i in [parenStack, bracketStack, braceStack, seqStack]:
            if i < 0:
                return char

def findIllegalChars(corruptedLines):
    res = []
    for line in corruptedLines:
        illegalChar = findIllegalCharInLine(line)
        if illegalChar != None:
            res.append(illegalChar)
    return res

def main():
    inputFile = 'input.txt'
    lines = readFile(inputFile).splitlines()
    corruptedLines = findCorruptedLines(lines)
    print(f'corrupted lines = {corruptedLines}')
    illegalChars = findIllegalChars(corruptedLines)
    print(f'Illegal chars = {illegalChars}')
    scores = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    corruptedScore = sum(map(lambda x: scores[x], illegalChars))
    print(f'Corrupted Scores = {corruptedScore}')
    return 42

if __name__ == '__main__':
    main()