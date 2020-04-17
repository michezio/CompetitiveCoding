# B

''' SUBMITTED WRONG
# I misunderstood the problem at first, after
# I realized my mistake I correctly coded the solution
# but still thought the array had an even number of elements
# so this works perfectly but only for even length arrays

    arr.sort()

    first = arr[:L]
    second = arr[L:]
    first = first[::-1]

    new = []
    for i in range(L):
        new.append(first[i])
        new.append(second[i])
'''

CASES = int(input())

answers = []

while (CASES):
    CASES -= 1

    L = int(input())
    arr = [int(x) for x in input().split(" ")]

    arr.sort()
    new = []
    fwd = 0
    bwd = L-1
    while (fwd <= bwd):
        if fwd == bwd:
            new.append(arr[fwd])
            break
        else:
            new.append(arr[fwd])
            new.append(arr[bwd])
            fwd += 1
            bwd -= 1

    answers.append(new)

for ans in answers:
    print(" ".join([str(x) for x in ans[::-1]]))
