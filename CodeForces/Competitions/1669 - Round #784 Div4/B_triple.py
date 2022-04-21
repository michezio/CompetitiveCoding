TESTS = int(input())

for _ in range(TESTS):

    l = int(input())

    lis = list(map(int, input().split()))

    lis.sort()

    counter = 0
    pnum = -1

    for x in lis:
        if x == pnum:
            counter += 1
            if counter == 3:
                print(x)
                break
        else:
            pnum = x
            counter = 1

    else:
        print("-1")

