'''
WRONG ANSWER, DOESN'T GIVE THE MINIMUM NUMBER OF CHANGES
'''

TEST = int(input())

answers = []
for _ in range(TEST):
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    pairs = [[arr[i],arr[-i-1]] for i in range(n//2)]

    max_changes = n
    for i in range(n//2):
        changes = 0
        max_sum = sum(pairs[i])
        for j in range(n//2):
            if j == i:
                continue
            s = sum(pairs[j])
            if s == max_sum:
                continue
            else:
                if 1+min(pairs[j]) <= abs(max_sum-s) <= k+max(pairs[j]):
                    changes += 1
                else:
                    changes += 2
        max_changes = min(max_changes, changes)

    answers.append(max_changes)

for ans in answers:
    print(ans)