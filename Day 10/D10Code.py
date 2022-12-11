def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def Cycle(currentTotal, currentCycle, currentX, addToX=0, numCycles=1):
    total = currentTotal
    thisCycle = currentCycle
    xVal = currentX
    significantCycles = [20, 60, 100, 140, 180, 220]
    for i in range(numCycles):
        thisCycle += 1
        if thisCycle in significantCycles:
            strength = xVal * thisCycle
            print("Signal strength for cycle " + str(thisCycle) + " is: " + str(strength))
            total += strength

    xVal += addToX

    return total, thisCycle, xVal


def Cycle2(screen, pos, currentCycle, currentX, addToX=0, numCycles=1):
    thisCycle = currentCycle
    currentScreen = screen
    currentPosition = pos
    xVal = currentX
    for i in range(numCycles):
        thisCycle += 1
        if currentPosition[1] > 39 and currentPosition[0] < 5:
            currentPosition[0] += 1
            currentPosition[1] = 0
        if abs(currentPosition[1] - xVal) <= 1:
            currentScreen[currentPosition[0]] += "#"
        else:
            currentScreen[currentPosition[0]] += "."
        currentPosition[1] += 1


    xVal += addToX

    return currentScreen, currentPosition, thisCycle, xVal


def Part1():
    inputs = ReadInput()
    currentCycle = 0
    xVal = 1
    # signalStrength = xVal * cycle
    sumSignalStrength = 0

    for i in inputs:
        line = i.split()
        if line[0] == "noop":
            sumSignalStrength, currentCycle, xVal = Cycle(sumSignalStrength, currentCycle, xVal)
        elif line[0] == "addx":
            sumSignalStrength, currentCycle, xVal = Cycle(sumSignalStrength, currentCycle, xVal, addToX=int(line[1]), numCycles=2)

    print("Sum: " + str(sumSignalStrength))

def Part2():
    inputs = ReadInput()
    currentCycle = 0
    xVal = 1
    currentPosition = [0, 0]
    screen = ["", "", "", "", "", ""]

    for i in inputs:
        line = i.split()
        if line[0] == "noop":
            screen, currentPosition, currentCycle, xVal = Cycle2(screen, currentPosition, currentCycle, xVal)
        elif line[0] == "addx":
            screen, currentPosition, currentCycle, xVal = Cycle2(screen, currentPosition, currentCycle, xVal, addToX=int(line[1]), numCycles=2)

    for i in screen:
        print(i)

# Part1()
Part2()
