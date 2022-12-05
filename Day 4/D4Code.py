def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def DetermineInclusionP1(assignments):
    total = 0

    for a in range(0, len(assignments)):
        firstElf = assignments[a][0].split('-')
        secondElf = assignments[a][1].split('-')
        firstIn = False

        if int(firstElf[0]) in range(int(secondElf[0]), int(secondElf[1])+1):
            if int(firstElf[1]) in range(int(secondElf[0]), int(secondElf[1])+1):
                total += 1
                firstIn = True
        if not firstIn:
            if int(secondElf[0]) in range(int(firstElf[0]), int(firstElf[1])+1):
                if int(secondElf[1]) in range(int(firstElf[0]), int(firstElf[1])+1):
                    total += 1

    return total


def DetermineInclusionP2(assignments):
    total = 0

    for a in range(0, len(assignments)):
        firstElf = assignments[a][0].split('-')
        secondElf = assignments[a][1].split('-')

        if int(firstElf[0]) in range(int(secondElf[0]), int(secondElf[1])+1):
            total += 1
        elif int(firstElf[1]) in range(int(secondElf[0]), int(secondElf[1])+1):
            total += 1
        elif int(secondElf[0]) in range(int(firstElf[0]), int(firstElf[1])+1):
            total += 1
        elif int(secondElf[1]) in range(int(firstElf[0]), int(firstElf[1])+1):
            total += 1

    return total


def Part1():
    parsedInput = ReadInput()
    assignments = []

    for i in parsedInput:
        assignments.append(i.split(','))

    print(DetermineInclusionP1(assignments))


def Part2():
    parsedInput = ReadInput()
    assignments = []

    for i in parsedInput:
        assignments.append(i.split(','))

    print(DetermineInclusionP2(assignments))


# Part1()
Part2()
