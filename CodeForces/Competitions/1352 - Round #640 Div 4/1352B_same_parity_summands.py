TEST = int(input())

answers = []
for _ in range(TEST):
    n, k = [int(x) for x in input().split()]

    if (n % 2 == 1 and k % 2 == 0)  \
            or (k > n):
        answers.append("NO")
    elif n == k:
        answers.append('YES\n' + '1 '*k)
    elif (n % 2 == 1 and k % 2 == 1)  \
            or (n % 2 == 0 and k % 2 == 0):
        answers.append('YES\n' + '1 '*(k-1) + str(n-k+1))
    else:
        if n >= k*2:
            answers.append('YES\n' + '2 '*(k-1) + str(n-2*(k-1)))
        else:
            answers.append("NO")

for ans in answers:
    print(ans)
