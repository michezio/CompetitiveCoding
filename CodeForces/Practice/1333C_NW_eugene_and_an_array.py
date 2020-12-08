# https://codeforces.com/problemset/problem/1333/C
# 1333C Eugene and an Array

''' NOT WORKING PROPERLY.... '''

L = int(input())
arr = [int(x) for x in input().split(" ")]

initial = 0
while(arr[initial] == 0):
    initial += 1
final = len(arr)-1
while(arr[final] == 0):
    final -= 1
arr = arr[initial:final+1]

L = len(arr)
total = L - arr.count(0)

if total == 0:
    print(0)
    exit()


dp = []
for x in range(L+1):
    dp.append([])
    for i in range(L+1):
        dp[x].append(None)


def checkSubarray(begin, end):
    global total
    if dp[begin][end] is not None:
        return dp[begin][end]
    elif (len(arr[begin:end]) == 1):
        isNotZero = arr[begin] != 0
        dp[begin][end] = isNotZero
        return isNotZero
    else:
        res = checkSubarray(begin, end-1) and checkSubarray(begin+1, end)
        s = sum(arr[begin:end])
        res = res and (s != 0)
        dp[begin][end] = res
        total += 1 if res else 0
        return res


res = checkSubarray(0, len(arr))

print(total)
