TESTS = int(input())

for _ in range(TESTS):

    size = int(input())
    seq = list(map(int, input().split()))

    deq = [seq.pop(0)]

    for el in seq:
        if el < deq[0]:
            deq.insert(0, el)
        else:
            deq.append(el)

    print(*deq)
