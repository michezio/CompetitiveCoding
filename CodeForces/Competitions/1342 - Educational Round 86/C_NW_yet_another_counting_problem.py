'''
NOT WORKING
'''

TESTS = int(input())

answers = []

for _ in range(TESTS):
    a, b, q = [int(x) for x in input().split()]
    fun = None
    if a > b:
        fun = lambda i: (i % a) % b != i % b  # noqa: E731
    else:
        fun = lambda i: i % a != (i % b) % a  # noqa: E731
    answers.append([])
    for _ in range(q):
        l, r = [int(x) for x in input().split()]
        if a == b:
            answers[-1].append(r-l+1)
        count = 0
        num = l
        stat = fun(num)
        cycle = 0
        total = 0
        remainder = False
        while (num <= r):
            res = fun(num)
            if res == stat:
                count += res
                num += 1
            if res != stat and not remainder:
                stat = res
                tops = 0
                while(tops < 2 and num <= r):
                    res = fun(num)
                    num += 1
                    total += res
                    cycle += 1
                    if res != stat:
                        tops += 1
                        stat = res
                while (num <= r):
                    num += cycle
                    count += total
                if num == r:
                    break
                else:
                    num -= cycle
                    count -= total
                    remainder = True
                    stat = res

        answers[-1].append(count)

for ans in answers:
    print(*ans)
