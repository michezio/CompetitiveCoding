# https://codeforces.com/problemset/problem/1331/B
# 1331B Limericks

n = int(input())

res = ""
for div in range(2, n//2 + 1):
    if (n % div == 0):
        res = str(div) + str(n//div)
        break

print(res)
