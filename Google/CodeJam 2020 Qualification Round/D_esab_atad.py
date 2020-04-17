import random

TEST, SIZE = [int(x) for x in input().split(" ")]

REQUESTS = 8
CHECKS = 2

DEBUG = True


def convert(index):
    if index >= 0:
        return index
    else:
        return SIZE + index


def update(ans, index, value):
    for a in ans:
        a[index] = value


def expand(ans):
    lim = len(ans)
    for i in range(lim):
        a = ans[i]
        b = [
            list(a[::-1]),
            list([int(not x) if x is not None else None for x in a]),
            list([int(not x) if x is not None else None for x in a[::-1]])
        ]
        for c in b:
            if (c not in ans):
                ans.append(c)
    if DEBUG:
        print("EXPANDED: {} -> {}".format(lim, len(ans)))


def collapse(ans, index, value):
    lim = len(ans)
    for i in range(lim-1, -1, -1):
        if (ans[i][index] != value):
            ans.pop(i)
    if DEBUG:
        print("COLLAPSED: {} -> {}".format(lim, len(ans)))


while (TEST):
    TEST -= 1

    if (SIZE == 10):
        ans = ""
        for i in range(1, SIZE+1):
            print(i)
            info = input()
            ans += info
        print(ans)
        if (input() == 'Y'):
            continue
        else:
            break

    if (SIZE > 10):
        ans = [[None for x in range(SIZE)]]
        limit = SIZE
        pos = -1
        query = 0
        completed = False
        check = 'Y'
        while (query <= 150):
            query += 1
            if DEBUG:
                print("@@@@@@@@@@@@@@@@")
                for a in ans:
                    print(a)
            if not completed:
                if (query > 2 and query % 10 in [1, 2]):
                    if (query % 10 == 1):
                        expand(ans)
                    if DEBUG:
                        print("CHECK QUERY #{}".format(query))
                    rind = 0
                    while True:
                        rind = random.randint(-pos, pos)
                        ck = []
                        for x in ans:
                            ck.append(x[rind])
                        if sum(ck) not in [0, len(ck)] or len(ans) == 1:
                            break
                    print(convert(rind)+1)
                    info = int(input())
                    collapse(ans, rind, info)
                else:
                    pos += 1
                    if (query % 2 == 0):
                        pos = -pos
                    else:
                        pos = -pos - 1
                    if DEBUG:
                        print("QUERY #{}".format(query))
                    print(convert(pos)+1)
                    info = int(input())
                    update(ans, pos, info)
                if (None not in ans[0]):
                    completed = True
            else:
                if (len(ans) == 1):
                    print("".join([str(x) for x in ans[0]]))
                    check = input()
                    if (check == 'Y'):
                        break
                    else:
                        exit()
                else:
                    if (query % 10 == 1):
                        expand(ans)
                    while True:
                        pos = random.randint(0, SIZE-1)
                        ck = []
                        for x in ans:
                            ck.append(x[pos])
                        if sum(ck) not in [0, len(ck)] or len(ans) == 1:
                            break
                    if DEBUG:
                        print("FINAL CHECK #{}".format(query))
                    print(convert(pos)+1)
                    value = int(input())
                    collapse(ans, pos, value)
