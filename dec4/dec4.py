

# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def makeBoards(lines):
    res = []
    currBoard = []
    for line in lines:
        if line == '' and currBoard != []:
            try:
                assert(len(currBoard) == 5)
                res.append(currBoard)
                currBoard = []
            except:
                print("currBoard:")
                print(currBoard)
                raise AssertionError
        else:
            currLine = list(map(lambda x: int(x), line.split()))
            currBoard.append(currLine) if currLine != [] else None
    if currBoard != res[-1]:
        res.append(currBoard)
    return res

def updateBoards(number, bingoBoards, boards, boardSets):
    # too much space
    for i in range(len(boards)):
        if number in boardSets[i]:
            for row in range(len(boards[i])):
                for col in range(len(boards[row])):
                    if boards[i][row][col] == number:
                        bingoBoards[i][row][col] = number
    

def makeBoardSets(boards):
    sets = []
    for board in boards:
        boardSet = set()
        for row in board:
            for col in row:
                boardSet.add(col)
        sets.append(boardSet)
    for i in range(len(boards)):
        for row in boards[i]:
            for elem in row:
                assert(elem in sets[i])
    return sets

def makeCols(board):
    res = []
    for col in range(len(board[0])):
        column = []
        for row in range(len(board)):
            column.append(board[row][col])
        res.append(column)
    return res

def checkWin(bingoBoard):
    # cols = [[bingoBoard[row][col] for row in range(len(bingoBoard))] for col in range(len(bingoBoard[0]))]
    cols = makeCols(bingoBoard)
    for row in bingoBoard:
        if None not in row:
            print(row)
            return row
    for col in cols:
        if None not in col:
            print(col)
            return col
    return []


def findWinner(bingoBoards):
    for i in range(len(bingoBoards)):
        res = checkWin(bingoBoards[i])
        if res != []:
            return i
    return -1

def getScore(number, bingoBoard, board):
    '''
    The score of the winning board can now be calculated. 
    Start by finding the sum of all unmarked numbers on that board; 
    in this case, the sum is 188. Then, multiply that sum by the number 
    that was just called when the board won, 24, to get the final score, 
    188 * 24 = 4512.
    '''
    unmarkedSum = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if bingoBoard[row][col] == None:
                print(board[row][col])
                unmarkedSum += board[row][col]
    return unmarkedSum * number

def findBestScore(numbers, boards):
    rows = len(boards[0])
    cols = len(boards[0][0])
    bingoBoards = [[[None] * cols for row in range(rows)] for board in range(len(boards))]
    boardSets = makeBoardSets(boards)
    for i in range(len(bingoBoards)):
        assert(len(bingoBoards[i]) == len(boards[i]))
        assert(len(bingoBoards[i][0]) == len(boards[i][0]))
    for number in numbers:
        # work through each number in the list, find it in each of the other lists 
        # and modify bingo boards to track winners
        # after each number, check for winners
        # if winners found, tally score and return
        updateBoards(number, bingoBoards, boards, boardSets)
        winningIndex = findWinner(bingoBoards)
        if winningIndex != -1:
            # print(number)
            # print("Bingo board: ")
            # for row in bingoBoards[i]:
            #     print(row)
            print(bingoBoards[winningIndex])
            # print("Board: ")
            # for row in boards[i]:
            #     print(row)
            # print(boards[i])
            score = getScore(number, bingoBoards[winningIndex], boards[winningIndex])
            return score

'''
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, 
so rather than waste time counting its arms, the safe thing to do is to figure 
out which board will win last and choose that one. That way, no matter which 
boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 
13 is eventually called and its middle column is completely marked. If you were 
to keep playing until this point, the second board would have a sum of unmarked 
numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
'''

def partTwo(numbers, boards):
    rows = len(boards[0])
    cols = len(boards[0][0])
    bingoBoards = [[[None] * cols for row in range(rows)] for board in range(len(boards))]
    boardSets = makeBoardSets(boards)
    for number in numbers:
        # work through each number in the list, find it in each of the other lists 
        # and modify bingo boards to track winners
        # after each number, check for winners
        # if winners found, tally score and return
        updateBoards(number, bingoBoards, boards, boardSets)
        winningIndex = findWinner(bingoBoards)
        if winningIndex != -1:
            lastNumber = number
            lastBingoBoard = bingoBoards[winningIndex]
            lastBoard = boards[winningIndex]
            bingoBoards.pop(winningIndex)
            boards.pop(winningIndex)
            boardSets.pop(winningIndex)


    score = getScore(lastNumber, lastBingoBoard, lastBoard)
    return score


def main():
    fileName = 'input.txt'
    contents = readFile(fileName)
    lines = contents.splitlines()
    numbers = list(map(lambda x: int(x), lines[0].split(',')))
    boards = makeBoards(lines[1:])
    # boards is a list of 2d lists
    bestScore = findBestScore(numbers, boards)
    lastWin = partTwo(numbers, boards)
    print(bestScore)
    print(f'lastWin = {lastWin}')

if __name__ == '__main__':
    main()