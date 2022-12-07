def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def Part1():
    # Sum of dirs that contain at leas 100,000 (dir <= 100,000)
    maxVal = 100000
    fullInput = ReadInput()
    dirs = {}
    directoryTracker = []
    clearedDirs = []
    dirPlaceMarker = 0
    for r in fullInput:
        line = r.split()

        if line[0] + line[1] == "$cd":
            if line[2] == "/":
                dirPlaceMarker = 0
                for i in directoryTracker:
                    clearedDirs.append(i)
                directoryTracker.clear()
            elif line[2] == "..":
                dirPlaceMarker -= 1
                clearedDirs.append(directoryTracker.pop(len(directoryTracker)-1))
            else:
                dirPlaceMarker += 1
                if line[1] not in dirs.keys():
                    directoryTracker.append([line[2], 0])
        elif line[0] == "dir":
            dirs[line[1]] = 0
        elif line[0] + line[1] == "$ls":
            pass
        else:
            for i in directoryTracker:
                i[1] += int(line[0])

    for i in directoryTracker:
        clearedDirs.append(i)

    sum = 0
    for d in clearedDirs:
        print(d)
        if d[1] <= maxVal:
            sum += int(d[1])

    print(sum)


def Part2():
    # 70,000,000
    totalDiscSpace = 70000000
    # 30,000,000
    unusedSpaceNeeded = 30000000

    fullInput = ReadInput()
    dirs = {}
    directoryTracker = [["/", 0]]
    clearedDirs = []
    dirPlaceMarker = 0

    for r in fullInput:
        line = r.split()

        if line[0] + line[1] == "$cd":
            if line[2] == "/":
                dirPlaceMarker = 0
                directoryTracker, clearedDirs = ClearToBaseDir(directoryTracker, clearedDirs)
            elif line[2] == "..":
                dirPlaceMarker -= 1
                clearedDirs.append(directoryTracker.pop())
            else:
                dirPlaceMarker += 1
                if line[1] not in dirs.keys():
                    directoryTracker.append([line[2], 0])
        elif line[0] == "dir":
            if line[1] not in dirs.keys():
                dirs[line[1]] = 0
        elif line[0] + line[1] == "$ls":
            pass
        else:
            for i in directoryTracker:
                i[1] += int(line[0])

    for i in directoryTracker:
        clearedDirs.append(i)

    usedSpace = directoryTracker[0][1]
    unusedSpace = totalDiscSpace - usedSpace
    spaceToClear = abs(unusedSpaceNeeded - unusedSpace)

    print("Unused space: " + str(unusedSpace))
    print("Used space: " + str(usedSpace))
    print("Space to clear: " + str(spaceToClear))

    potentialDirs = []
    for d in clearedDirs:
        if int(d[1]) >= spaceToClear:
            print(d)
            potentialDirs.append(d)

    smallestDir = potentialDirs[0]
    for i in potentialDirs:
        if int(i[1]) < int(smallestDir[1]):
            smallestDir = i

    print("Delete: ")
    print(smallestDir)


def ClearToBaseDir(arr, insertTo):
    toTake = arr
    newArr = insertTo

    while len(toTake) > 1:
        newArr.append(toTake.pop())

    return toTake, newArr

# Part1()
Part2()
