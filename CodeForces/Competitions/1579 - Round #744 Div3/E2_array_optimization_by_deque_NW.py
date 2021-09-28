''' TIME LIMIT EXCEEDED, BUT IS WORKING '''

TESTS = int(input())

for _ in range(TESTS):

    size = int(input())
    seq = list(map(int, input().split()))

    deq = [seq.pop(0)]

    def countInv(el, deq):
        countL = 0
        countR = 0
        for i in deq:
            if el > i:
                countL += 1
            elif el < i:
                countR += 1
        return countL, countR

    invs = 0

    for el in seq:
        L, R = countInv(el, deq)
        #print(f"({L}) {el} -> {deq} <- {el} ({R})")
        if L < R:
            deq.insert(0, el)
            invs += L
        elif R < L:
            deq.append(el)
            invs += R
        else:
            if el < deq[0]:
                deq.insert(0, el)
            else:
                deq.append(el)
            invs += L

    #print(f"RESULT: {deq} with {invs} inversions")
    print(invs)
