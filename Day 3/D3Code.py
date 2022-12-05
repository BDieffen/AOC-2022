def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


# Same number of items in each compartment
# first half of characters on a line is the first compartment
# second half of characters on a line is the second compartment

# Priorities
# a-z = 1-26
# A-Z = 27-52

def GetCharPriority(char):
    prio = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    if char.islower():
        return prio.get(char.lower())
    else:
        return prio.get(char.lower()) + 26


def FindMatchingItemPart1(compartment1, compartment2):
    for c1 in compartment1:
        for c2 in compartment2:
            if c1 == c2:
                return GetCharPriority(c1)


def FindMatchingItemPart2(pack1, pack2, pack3):
    for i1 in pack1:
        for i2 in pack2:
            if i1 == i2:
                for i3 in pack3:
                    if i2 == i3:
                        return GetCharPriority(i3)


def Part1():
    rucksacks = ReadInput()
    totalSum = 0

    for r in rucksacks:
        firstCompartment = []
        secondCompartment = []
        numItems = len(r)
        # Split the entire rucksack into compartments
        for i in range(numItems):
            if i < (numItems/2):
                firstCompartment.append(r[i])
            else:
                secondCompartment.append(r[i])
        totalSum += FindMatchingItemPart1(firstCompartment, secondCompartment)

    print("Part 1 answer: " + str(totalSum))


def Part2():
    rucksacks = ReadInput()
    totalSum = 0

    for r in range(0, len(rucksacks), 3):
        firstElf = rucksacks[r]
        secondElf = rucksacks[r+1]
        thirdElf = rucksacks[r+2]
        totalSum += FindMatchingItemPart2(firstElf, secondElf, thirdElf)

    print("Part 2 answer: " + str(totalSum))


Part1()
Part2()
