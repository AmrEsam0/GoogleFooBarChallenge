def solution(l):
    sum = 0
    for i in range(1, len(l)):
        x = getFactors(i, l)
        y = getMultiples(i, l)
        sum += x * y
        i += 1

    return sum


def getFactors(index, l):
    sum = 0
    for i in range(0, index):
        if l[index] % l[i] == 0:
            sum += 1
    return sum


def getMultiples(index, l):
    sum = 0
    for i in range(index+1, len(l)):
        if l[i] % l[index] == 0:
            sum += 1
    return sum
