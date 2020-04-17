# not working, it's not the lexicographically smallest sequence

CASES = int(input())

answers = []

while (CASES):
    CASES -= 1

    num, begin, end = [int(x) for x in input().split(" ")]

    sequence = []

    index = 0
    tempB = begin
    tempE = end
    while (tempB > 0):
        tempB -= 2*index
        tempE -= 2*index
        index += 1

    if (tempB < 0):
        index -= 1
        tempB += 2*index
        tempE += 2*index

    i = 0
    while (i <= tempE):
        for x in range(1, index + 1):
            sequence.append(x)
            sequence.append(index + 1)
            i += 2
        index += 1

    tempE = tempE if tempE > tempB else (tempB)
    answers.append(" ".join([str(x) for x in sequence[tempB - 1:tempE]]))

for ans in answers:
    print(ans)
