def ReadInput():
    with open('input.txt') as f:
        return f.read()


def Checker(arr):

    for i in range(len(arr)-1):
        if arr.count(arr[i]) > 1:
            return False
    return True


def Part1():
    scrambled = ReadInput()
    marker = []
    startIndex = 3
    for c in scrambled:
        if len(marker) < 4:
            marker.append(c)
        else:
            if not Checker(marker):
                print(marker)
                marker.pop(0)
                marker.append(c)
                startIndex += 1

    # startIndex = scrambled.index(marker[len(marker)-1])+1
    print(str(startIndex+1))


def Part2():
    scrambled = ReadInput()
    startOfMessage = []
    startIndex = 13
    for c in scrambled:
        if len(startOfMessage) < 14:
            startOfMessage.append(c)
        else:
            if not Checker(startOfMessage):
                print(startOfMessage)
                startOfMessage.pop(0)
                startOfMessage.append(c)
                startIndex += 1

    # startIndex = scrambled.index(marker[len(marker)-1])+1
    print(str(startIndex+1))


# Part1()
Part2()
