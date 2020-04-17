w = int(input())

ans = []

while(w):
    w -= 1
    n = int(input())
    matrix = []
    k = 0
    r = 0
    c = 0
    for i in range(n):
        matrix.append([int(x) for x in input().split(" ")])
        unique = set(matrix[i])
        if len(unique) < n:
            r += 1
        k += matrix[i][i]
    for i in range(n):
        unique = set([x[i] for x in matrix])
        if (len(unique) < n):
            c += 1
    ans.append([k, r, c])

for i in range(len(ans)):
    a = ans[i]
    print("Case #{}: {} {} {}".format(i+1, a[0], a[1], a[2]))
