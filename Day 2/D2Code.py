def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


# First column = what opponent will play
# A = Rock = 1 point
# B = Paper = 2 points
# C = Scissors = 3 points
# **PART 1**
# Second column = what I should play
# X = Rock
# Y = Paper
# Z = Scissors
# **PART 2**
# Second column = Required outcome
# X = Lose
# Y = Draw
# Z = Win

# Scoring
# My selection
# Rock = 1 point
# Paper = 2 points
# Scissors = 3 points
#########################
# Outcome of round
# lost = 0 points
# draw = 3 points
# won = 6 points


def part1():
    totalScore = 0
    inputList = ReadInput()

    for line in inputList:
        separated = line.split(' ')

        if separated[0] == 'A':
            if separated[1] == 'X':
                totalScore += 1
                # DRAW
                totalScore += 3
            elif separated[1] == 'Y':
                totalScore += 2
                # WIN
                totalScore += 6
            else:  # Z
                totalScore += 3
                # LOSS
        elif separated[0] == 'B':
            if separated[1] == 'X':
                totalScore += 1
                # LOSS
            elif separated[1] == 'Y':
                totalScore += 2
                # DRAW
                totalScore += 3
            else:  # Z
                totalScore += 3
                # WIN
                totalScore += 6
        else:  # C
            if separated[1] == 'X':
                totalScore += 1
                # WIN
                totalScore += 6
            elif separated[1] == 'Y':
                totalScore += 2
                # LOSS
            else:  # Z
                totalScore += 3
                # DRAW
                totalScore += 3

    print(totalScore)


def part2():
    totalScore = 0
    inputList = ReadInput()

    for line in inputList:
        separated = line.split(' ')

        if separated[0] == 'A':
            if separated[1] == 'X':
                totalScore += 3
                # LOSS
            elif separated[1] == 'Y':
                totalScore += 1
                # DRAW
                totalScore += 3
            else:  # Z
                totalScore += 2
                # WIN
                totalScore += 6
        elif separated[0] == 'B':
            if separated[1] == 'X':
                totalScore += 1
                # LOSS
            elif separated[1] == 'Y':
                totalScore += 2
                # DRAW
                totalScore += 3
            else:  # Z
                totalScore += 3
                # WIN
                totalScore += 6
        else:  # C
            if separated[1] == 'X':
                totalScore += 2
                # LOSS
            elif separated[1] == 'Y':
                totalScore += 3
                # DRAW
                totalScore += 3
            else:  # Z
                totalScore += 1
                # WIN
                totalScore += 6

    print(totalScore)


# part1()
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
part2()
