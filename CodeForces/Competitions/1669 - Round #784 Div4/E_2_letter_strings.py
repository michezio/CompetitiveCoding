from collections import defaultdict

TESTS = int(input())

for _ in range(TESTS):

    l = int(input())

    def init():
        return 0

    strings = defaultdict(init)
    start_strings = defaultdict(init)
    end_strings = defaultdict(init)

    counter = 0

    for _ in range(l):
        s = input()
        a, b = s

        counter += start_strings[a] + end_strings[b] - 2*strings[s]

        strings[s] += 1
        start_strings[a] += 1
        end_strings[b] += 1

    print(counter)

'''
OLD VERSION, TLE

import itertools


def congrue(a, b):
    cond1 = a & 0xF0 == b & 0xF0
    cond2 = a & 0xF == b & 0xF
    return cond1 ^ cond2

TESTS = int(input())

for _ in range(TESTS):

    l = int(input())

    strings = []
    counters = []

    prev = ""
    for _ in range(l):
        s = input()
        if s == prev:
            counters[-1] += 1
        else:
            prev = s
            counters.append(1)
            num = int(bin(16 + ord(s[0]) - ord('a'))[3:] + bin(16 + ord(s[1]) - ord('a'))[3:], 2)
            strings.append(num)

    print(sum(counters[i]*counters[j]*congrue(strings[i], strings[j]) for i, j in itertools.combinations(range(len(strings)), 2)))
'''
