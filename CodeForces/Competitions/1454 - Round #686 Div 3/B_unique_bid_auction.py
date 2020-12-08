TEST = int(input())

answers = []
for _ in range(TEST):
    n = int(input())
    chosen = [int(x) for x in input().split()]

    lis = [[] for _ in range(n+1)]

    for i, p in enumerate(chosen):
        lis[p].append(i)

    nlis = [x[0] for x in lis if len(x) == 1]

    ans = nlis[0]+1 if len(nlis) > 0 else -1

    answers.append(ans)

for ans in answers:
    print(ans)
