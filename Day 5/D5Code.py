def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def GetStacks(inputs, numStacks):
    stacks = []
    placement = 1
    indexArr = [1, 5, 9, 13, 17, 21, 25, 29, 33]

    for i in range(numStacks):
        stacks.append(inputs[i])

    stacks.reverse()
    # for s in stacks:
    #     print(s)
    #
    # print("-----------------------------------------")

    arr = []
    for i in range(numStacks):
        arr.append([])

    for i in range(numStacks):
        for s in stacks:
            # print(i)
            # print(s[indexArr[i]])
            arr[i].append(s[indexArr[i]])
        placement += 3

    # for a in arr:
    #     print(a)

    return arr

def GetProcedures(inputs):
    procedures = []

    for i in range(10, len(inputs)):
        procedures.append(inputs[i])
        # print(inputs[i])

    return procedures


def ActivateProceduresP1(procedures, stacks):
    newStack = stacks
# 1 : number of crates to move
# 3 : from this stack
# 5: to this stack

    for r in newStack:
        while(" " in r):
            r.remove(" ")

    for p in procedures:
        line = p.split(" ")
        for i in range(int(line[1])):
            stackNum = int(line[3]) - 1
            moveToStack = int(line[5]) - 1
            # lastIndexUsed = newStack[stackNum].index([j for j in newStack[stackNum] if j][-1])
            lastIndexUsed = len(newStack[stackNum])-1

            currentBox = newStack[stackNum].pop(lastIndexUsed)

            newStack[moveToStack].append(currentBox)

    return newStack


def ActivateProceduresP2(procedures, stacks):
    newStack = stacks
# 1 : number of crates to move
# 3 : from this stack
# 5: to this stack

    for r in newStack:
        while(" " in r):
            r.remove(" ")


    for p in procedures:
        line = p.split(" ")
        stackNum = int(line[3]) - 1
        moveToStack = int(line[5]) - 1
        boxes = []

        for i in range(int(line[1])):
            lastIndexUsed = len(newStack[stackNum])-1
            box = newStack[stackNum].pop(lastIndexUsed)
            boxes.append(box)

        boxes.reverse()
        newStack[moveToStack] += boxes
    return newStack


def Part1():
    inputs = ReadInput()
    answer = ""
    stacks = GetStacks(inputs, 9)
    procedures = GetProcedures(inputs)

    stack = ActivateProceduresP1(procedures, stacks)
    for r in stack:
        print(r)
        answer += r[len(r)-1]

    print(answer)


def Part2():
    inputs = ReadInput()
    answer = ""
    stacks = GetStacks(inputs, 9)
    procedures = GetProcedures(inputs)

    stack = ActivateProceduresP2(procedures, stacks)
    for r in stack:
        print(r)
        answer += r[len(r)-1]

    print(answer)


# Part1()
Part2()
