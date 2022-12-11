def ReadInput():
    with open('sampleinput2.txt') as f:
        return f.read().splitlines()


def ReadInstructions(input, grid, hLoc, tLoc, t):
    newGrid = grid
    head = hLoc
    tailStartLoc = tLoc
    numTails = t
    tails = []

    for i in range(numTails):
        tails.append([tLoc[0], tLoc[1]])

    newGrid = MarkTailNode(newGrid, tailStartLoc)

    for line in input:
        movement = line.split()
        direction = movement[0]
        steps = int(movement[1])

        DrawGridWithTails(newGrid, tails)
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        if direction == "U":
            newGrid, head, tails = MoveUp(newGrid, steps, head, tails)
        elif direction == "D":
            newGrid, head, tails = MoveDown(newGrid, steps, head, tails)
        elif direction == "L":
            newGrid, head, tails = MoveLeft(newGrid, steps, head, tails)
        else:
            newGrid, head, tails = MoveRight(newGrid, steps, head, tails)

    return newGrid


def MoveUp(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tails = tail

    for i in range(stepsRemaining):
        headY -= 1
        for j, t in enumerate(tails):
            tailX = t[1]
            tailY = t[0]
            if j is not 0:
                leadX = tails[j-1][1]
                leadY = tails[j-1][0]
                if abs(tailY - leadY) > 1 and abs(tailX - leadX) >= 1:
                    t[0] = leadY + 1
                    t[1] = leadX
                elif abs(tailY - leadY) > 1:
                    t[0] = leadY + 1
            else:
                if abs(tailY - headY) > 1 and abs(tailX - headX) >= 1:
                    t[0] = headY + 1
                    t[1] = headX
                elif abs(tailY - headY) > 1:
                    t[0] = headY + 1
            if j == len(tails)-1:
                newGrid = MarkTailNode(newGrid, t)

    newHead = [headY, headX]
    return newGrid, newHead, tails


def MoveDown(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tails = tail

    for i in range(stepsRemaining):
        headY += 1
        for j, t in enumerate(tails):
            tailX = t[1]
            tailY = t[0]
            if j is not 0:
                leadX = tails[j-1][1]
                leadY = tails[j-1][0]
                if abs(tailY - leadY) > 1 and abs(tailX - leadX) >= 1:
                    t[0] = leadY - 1
                    t[1] = leadX
                elif abs(tailY - leadY) > 1:
                    t[0] = leadY - 1
            else:
                if abs(tailY - headY) > 1 and abs(tailX - headX) >= 1:
                    t[0] = headY - 1
                    t[1] = headX
                elif abs(tailY - headY) > 1:
                    t[0] = headY - 1
            if j == len(tails)-1:
                newGrid = MarkTailNode(newGrid, t)

    newHead = [headY, headX]
    return newGrid, newHead, tails


def MoveLeft(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tails = tail

    for i in range(stepsRemaining):
        headX -= 1
        for j, t in enumerate(tails):
            tailX = t[1]
            tailY = t[0]
            if j is not 0:
                leadX = tails[j-1][1]
                leadY = tails[j-1][0]
                if abs(tailX - leadX) > 1 and abs(tailY - leadY) >= 1:
                    t[1] = leadX + 1
                    t[0] = leadY
                elif abs(tailX - leadX) > 1:
                    t[1] = leadX + 1
            else:
                if abs(tailX - headX) > 1 and abs(tailY - headY) >= 1:
                    t[1] = headX + 1
                    t[0] = headY
                elif abs(tailX - headX) > 1:
                    t[1] = headX + 1
            if j == len(tails)-1:
                newGrid = MarkTailNode(newGrid, t)

    newHead = [headY, headX]

    return newGrid, newHead, tails


def MoveRight(grid, steps, head, tail):
    newGrid = grid
    stepsRemaining = steps
    headX = head[1]
    headY = head[0]
    tails = tail

    for i in range(stepsRemaining):
        headX += 1
        for j, t in enumerate(tails):
            tailX = t[1]
            tailY = t[0]
            if j is not 0:
                leadX = tails[j-1][1]
                leadY = tails[j-1][0]
                if abs(tailX - leadX) > 1 and abs(tailY - leadY) >= 1:
                    t[1] = leadX - 1
                    t[0] = leadY
                if abs(tailX - leadX) > 1:
                    t[1] = leadX - 1
            else:
                if abs(tailX - headX) > 1 and abs(tailY - headY) >= 1:
                    t[1] = headX - 1
                    t[0] = headY
                if abs(tailX - headX) > 1:
                    t[1] = headX - 1
            if j == len(tails)-1:
                newGrid = MarkTailNode(newGrid, t)

    newHead = [headY, headX]
    return newGrid, newHead, tails


def MarkTailNode(grid, tail):
    newGrid = grid
    newGrid[int(tail[0])][int(tail[1])] = 0
    return newGrid


def CheckTouchedNodes(grid):
    total = 0
    for i in grid:
        for j in i:
            if j == 1:
                total += 1
        print(i)

    return total


def DrawGridWithTails(grid, tails):
    tempGrid = grid
    for i, tail in enumerate(tails):
        tempGrid[int(tail[0])][int(tail[1])] = i+1

    for i in tempGrid:
        print(i)


def MakeGrid(r, c):
    arr = []
    rows = r
    cols = c

    for i in range(rows):
        arr.append([])
        for j in range(cols):
            arr[i].append(0)

    return arr


def Part2(h, l, t):
    grid = MakeGrid(h, l)
    inputs = ReadInput()
    hLoc = [(h/2)-1, (l/2)-1]
    tLoc = [(h/2)-1, (l/2)-1]
    numTails = t

    grid = ReadInstructions(inputs, grid, hLoc, tLoc, numTails)
    print(CheckTouchedNodes(grid))


Part2(30,30, 9)
