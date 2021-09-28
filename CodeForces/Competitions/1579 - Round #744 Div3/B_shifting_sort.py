TESTS = int(input())

for _ in range(TESTS):
    size = int(input())
    arr = list(map(int, input().split()))
    fullarr = []
    op = []
    l = 0
    while (l < size):
        r = arr.index(min(arr))
        if (r > 0):
            d = r
            op.append(f"{l+1} {r+l+1} {d}")
        fullarr.append(arr.pop(r))
        l += 1

    print(len(op))
    for s in op:
        print(s)
