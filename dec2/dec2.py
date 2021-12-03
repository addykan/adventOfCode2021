
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def parseInstructions(instructions):
    depth = 0
    length = 0
    for line in instructions:
        if line == '':
            continue
        direction, number = line.split()
        number = int(number)
        match direction:
            case 'forward':
                length += number
            case 'up':
                depth -= number
            case 'down':
                depth += number
    print(f'Depth = {depth}, length = {length}, result = {depth * length}')


'''
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.

'''
def parseInstructionsPart2(instructions):
    aim = 0
    horizontal = 0
    depth = 0
    for line in instructions:
        if line == '':
            continue
        direction, number = line.split()
        number = int(number)
        match direction:
            case 'forward':
                horizontal += number
                depth += aim * number
            case 'up':
                aim -= number
            case 'down':
                aim += number
    print(f'Depth = {depth}, horizontal = {horizontal}, result = {depth * horizontal}')

def main():
    filePath = 'input.txt'
    instructions = readFile(filePath).splitlines()
    parseInstructions(instructions)
    parseInstructionsPart2(instructions)
    return 0


if __name__ == '__main__':
    main()
