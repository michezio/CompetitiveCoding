# C

from collections import Counter
from itertools import repeat, chain

cases = int(input())

ans = []

while(cases):
    cases -= 1
    n = int(input())
    students = [int(x) for x in input().split(" ")]
    cpy = students.copy()
    students = list(chain.from_iterable(repeat(i, c)
                    for i, c in Counter(cpy).most_common()))
    m = students[0]
    count = 0
    while (count < len(students) and m == students[count]):
        count += 1
    unique = set(students[count:])
    max_diff = len(unique)

    res = min(count, max_diff)

    if (count - max_diff > 1):
        res += 1

    ans.append(res)

for a in ans:
    print(a)
