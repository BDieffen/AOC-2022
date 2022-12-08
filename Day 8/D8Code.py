def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def GetBorderTrees(arr):
    length = len(arr[0])
    height = 0
    borderTotal = 0
    for i in arr:
        height += 1

    # Minus 4 for the corners (so we aren't counting them each twice)
    borderTotal += (length * 2) + (height * 2) - 4

    return borderTotal, length, height


def CalculateInnerVisibleTrees(arr, length, height):
    totalVisible = 0
    for i, row in enumerate(arr):
        if i != 0:
            if i != height-1:
                for j, col in enumerate(row):
                    if j != 0:
                        if j != length-1:
                            treeHeight = int(row[int(j)])
                            isTreeVisible = False
                            # If not the top row
                            if i > 0:
                                tallestTree = True
                                for k in range(0, i):
                                    if int(arr[k][j]) >= treeHeight:
                                        tallestTree = False
                                if tallestTree:
                                    isTreeVisible = True
                            # If not the far-left column
                            if j > 0 and not isTreeVisible:
                                tallestTree = True
                                for k in range(0, j):
                                    if int(arr[i][k]) >= treeHeight:
                                        tallestTree = False
                                if tallestTree:
                                    isTreeVisible = True
                            # If not the bottom row
                            if i < height-1 and not isTreeVisible:
                                tallestTree = True
                                for k in range(height-1, i, -1):
                                    if int(arr[k][j]) >= treeHeight:
                                        tallestTree = False
                                if tallestTree:
                                    isTreeVisible = True
                            # If not the far-right column
                            if j < length-1 and not isTreeVisible:
                                tallestTree = True
                                for k in range(length-1, j, -1):
                                    if int(arr[i][k]) >= treeHeight:
                                        tallestTree = False
                                if tallestTree:
                                    isTreeVisible = True

                            if isTreeVisible:
                                totalVisible += 1
    return totalVisible


def CalculateTreeScore(arr, length, height):
    highestTreeScore = 0
    for i, row in enumerate(arr):
        if i != 0:
            if i != height-1:
                for j, col in enumerate(row):
                    if j != 0:
                        thisTreeScore = 0
                        topViewScore = 0
                        rightViewScore = 0
                        bottomViewScore = 0
                        leftViewScore = 0
                        if j != length-1:
                            treeHeight = int(row[int(j)])
                            # If not the top row
                            if i > 0:
                                for k in range(i-1, -1, -1):
                                    topViewScore += 1
                                    if int(arr[k][j]) < treeHeight:
                                        continue
                                    else:
                                        break
                            # If not the far-left column
                            if j > 0:
                                for k in range(j-1, -1, -1):
                                    leftViewScore += 1
                                    if int(arr[i][k]) < treeHeight:
                                        continue
                                    else:
                                        break
                            # If not the bottom row
                            if i < height-1:
                                for k in range(i+1, height):
                                    bottomViewScore += 1
                                    if int(arr[k][j]) < treeHeight:
                                        continue
                                    else:
                                        break
                            # If not the far-right column
                            if j < length-1:
                                for k in range(j+1, length):
                                    rightViewScore += 1
                                    if int(arr[i][k]) < treeHeight:
                                        continue
                                    else:
                                        break

                            thisTreeScore = (topViewScore * leftViewScore * bottomViewScore * rightViewScore)
                            if thisTreeScore > highestTreeScore:
                                highestTreeScore = thisTreeScore

    return highestTreeScore


def Part1():
    fullInput = ReadInput()
    visible, forestLength, forestHeight = GetBorderTrees(fullInput)
    innerVisible = CalculateInnerVisibleTrees(fullInput, forestLength, forestHeight)

    print("Length: " + str(forestLength))
    print("Height: " + str(forestHeight))
    print("Total visible trees: " + str((visible + innerVisible)))


def Part2():
    fullInput = ReadInput()
    visible, forestLength, forestHeight = GetBorderTrees(fullInput)

    print("Length: " + str(forestLength))
    print("Height: " + str(forestHeight))
    print("Highest Tree Score: " + str(CalculateTreeScore(fullInput, forestLength, forestHeight)))


# Part1()
Part2()