CASES = int(input())

answers = []

while (CASES):
    CASES -= 1

    num, begin, end = [int(x) for x in input().split(" ")]

    sequence = []

    index = 1
    tempB = begin
    tempE = end
    temp = 2*(num - index)
    while (tempB > temp and index < num):
        tempB -= temp
        tempE -= temp
        index += 1
        temp = 2*(num - index)

    i = 0
    while (i < tempE and index <= num):
        if index == num:
            sequence.append(1)
            i += 1
        else:
            for x in range(index, num):
                sequence.append(index)
                sequence.append(x + 1)
                i += 2
        index += 1

    tempE = tempE if tempE > tempB else (tempB)
    answers.append(" ".join([str(x) for x in sequence[tempB - 1:tempE]]))

for ans in answers:
    print(ans)
