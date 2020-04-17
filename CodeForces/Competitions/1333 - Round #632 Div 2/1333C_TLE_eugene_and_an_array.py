# https://codeforces.com/problemset/problem/1333/C
# 1333C Eugene and an Array

''' TOO SLOW (TLE) '''

L = int(input())
arr = [int(x) for x in input().split(" ")]

initial = 0
while(initial < len(arr) and arr[initial] == 0):
    initial += 1
final = len(arr)-1
while(final >= 0 and arr[final] == 0):
    final -= 1
if final < initial:
    print(0)
    exit()

arr = arr[initial:final+1]

L = len(arr)
total = L - arr.count(0)

dp = []
for x in range(L+1):
    dp.append([])
    for i in range(L+1):
        dp[x].append(None)


for i in range(len(arr)):
    arr[i] = arr[i] + (arr[i-1] if i-1 >= 0 else 0)


def checkSubarray(begin, end):
    global total
    if dp[begin][end] is not None:
        return dp[begin][end]
    elif (len(arr[begin:end]) == 1):
        isNotZero = arr[begin] != (arr[begin-1] if begin-1 >= 0 else 0)
        dp[begin][end] = isNotZero
        return isNotZero
    else:
        res = checkSubarray(begin, end-1) and checkSubarray(begin+1, end)
        new = arr[end-1] != (0 if begin-1 < 0 else arr[begin-1])
        res &= new
        dp[begin][end] = res
        total += 1 if res else 0
        return res


checkSubarray(0, len(arr))

print(total)
