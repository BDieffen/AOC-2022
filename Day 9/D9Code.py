def ReadInput():
    with open('sampleinput.txt') as f:
        return f.read().splitlines()


def ReadInstructions(input, grid, hLoc, tLoc):
    newGrid = grid
    head = hLoc
    tail = tLoc

    newGrid = MarkTailNode(newGrid, tail)

    for line in input:
        movement = line.split()
        direction = movement[0]
        steps = int(movement[1])
        if direction == "U":
            newGrid, head, tail = MoveUp(grid, steps, head, tail)
        elif direction == "D":
            newGrid, head, tail = MoveDown(grid, steps, head, tail)
        elif direction == "L":
            newGrid, head, tail = MoveLeft(grid, steps, head, tail)
        else:
            newGrid, head, tail = MoveRight(grid, steps, head, tail)

    return newGrid


def MoveUp(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tailX = tail[1]
    tailY = tail[0]

    for i in range(stepsRemaining):
        headY -= 1
        if abs(tailY - headY) > 1 and abs(tailX - headX) >= 1:
            tailY = headY + 1
            tailX = headX
        elif abs(tailY - headY) > 1:
            tailY = headY + 1
        newGrid = MarkTailNode(newGrid, [tailY, tailX])

    newHead = [headY, headX]
    newTail = [tailY, tailX]
    return newGrid, newHead, newTail


def MoveDown(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tailX = tail[1]
    tailY = tail[0]

    for i in range(stepsRemaining):
        headY += 1
        if abs(tailY - headY) > 1 and abs(tailX - headX) >= 1:
            tailY = headY - 1
            tailX = headX
        elif abs(tailY - headY) > 1:
            tailY = headY - 1
        newGrid = MarkTailNode(newGrid, [tailY, tailX])

    newHead = [headY, headX]
    newTail = [tailY, tailX]

    return newGrid, newHead, newTail


def MoveLeft(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tailX = tail[1]
    tailY = tail[0]

    for i in range(stepsRemaining):
        headX -= 1
        if abs(tailX - headX) > 1 and abs(tailY - headY) >= 1:
            tailX = headX + 1
            tailY = headY
        if abs(tailX - headX) > 1:
            tailX = headX + 1
        newGrid = MarkTailNode(newGrid, [tailY, tailX])

    newHead = [headY, headX]
    newTail = [tailY, tailX]

    return newGrid, newHead, newTail


def MoveRight(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tailX = tail[1]
    tailY = tail[0]

    for i in range(stepsRemaining):
        headX += 1
        if abs(tailX - headX) > 1 and abs(tailY - headY) >= 1:
            tailX = headX - 1
            tailY = headY
        if abs(tailX - headX) > 1:
            tailX = headX - 1
        newGrid = MarkTailNode(newGrid, [tailY, tailX])

    newHead = [headY, headX]
    newTail = [tailY, tailX]

    return newGrid, newHead, newTail


def MarkTailNode(grid, tail):
    newGrid = grid
    newGrid[int(tail[0])][int(tail[1])] = 1
    return newGrid


def CheckTouchedNodes(grid):
    total = 0
    for i in grid:
        for j in i:
            if j == 1:
                total += 1

    return total


def MakeGrid(r, c):
    arr = []
    rows = r
    cols = c

    for i in range(rows):
        arr.append([])
        for j in range(cols):
            arr[i].append(0)

    return arr


def Part1(h, l):
    grid = MakeGrid(h, l)
    inputs = ReadInput()
    hLoc = [(h/2)-1, (l/2)-1]
    tLoc = [(h/2)-1, (l/2)-1]

    grid = ReadInstructions(inputs, grid, hLoc, tLoc)
    print(CheckTouchedNodes(grid))


Part1(1000, 1000)
