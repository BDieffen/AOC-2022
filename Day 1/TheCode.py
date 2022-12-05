def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def addTotalCals(lines):
    currentCalories = 0
    cals = []
    for line in lines:
        if line == '':
            cals.append(currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(line)

    return cals


def part1():
    caloriesCarried = addTotalCals(ReadInput())
    print(max(caloriesCarried))


def part2():
    total = 0
    caloriesCarried = addTotalCals(ReadInput())
    for i in range(3):
        total += max(caloriesCarried)
        caloriesCarried.pop(caloriesCarried.index(max(caloriesCarried)))
    print(total)


part1()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
part2()
