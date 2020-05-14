TEST = int(input())

answers = []
for _ in range(TEST):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    a.sort()
    b.sort(reverse=True)
    i = 0
    while k > 0:
        if a[i] > b[i]:
            break
        a[i], b[i] = b[i], a[i]
        i += 1
        k -= 1

    answers.append(sum(a))

for ans in answers:
    print(ans)
