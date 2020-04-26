TESTS = int(input())

answers = []

for _ in range(TESTS):
    x, y = [int(x) for x in input().split()]
    a, b = [int(x) for x in input().split()]

    if a == 0 or b == 0:
        answers.append(0)
    else:
        b = min(2*a, b)
        diff = abs(x - y)
        res = min(x, y) * b + diff * a
        answers.append(res)

for ans in answers:
    print(ans)
