# Day 3
def openFile(filePath: str = 'example3.txt') -> list:
    field = list()
    with open(filePath, 'r') as file:
        for line in file.readlines():
            field.append(line)
    return field

def slopes(field: list, direction: tuple) -> int:
    numOfRows = len(field)
    rowLength = len(field[0]) - 1
    countTrees = 0
    curPosX = 0
    xIncrement = direction[0]
    yIncrement = direction[1]

    for i in range(yIncrement, numOfRows, yIncrement):
        curPosX += xIncrement
        if (curPosX >= rowLength):
            curPosX = curPosX % rowLength
        if (field[i][curPosX] == '#'):
            countTrees += 1
    return countTrees


field = openFile()
print("Part 1: {0}".format(slopes(field,(3,1))))

# For Day 3 Part 2
result = 1
slopesDirection = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for i in range(len(slopesDirection)):
    result *= slopes(field, slopesDirection[i])
print("Part 2: {0}".format(result))