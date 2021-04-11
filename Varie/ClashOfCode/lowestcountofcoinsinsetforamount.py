import sys
import math

'''
Find the smallest amount of coins to use to reach the value given a set of coin values
'''

n = int(input()) # the amount to reach
s = int(input()) # the number of coins in set
coins = []
if s == 0:
    print(-1)
else:
    for i in input().split():
        vi = int(i) # the i-th coin value in set
        if vi not in coins:
            coins.append(vi)

    # find the smallest amount of coins to use
    # sort from greatest value to smallest
    coins.sort(reverse=True)
    rr = float("inf")
    k = 0
    # start from each coin value and go lower
    while k < len(coins):
        num = n
        i = k
        res = 0
        # try all coins untill you reach 0 or run out of coins
        while i < len(coins):
            while coins[i] <= num and num > 0:
                num -= coins[i]
                res += 1
            i += 1
        # if a smaller amount of coins is found update the rr (global result)
        if res > 0 and num == 0:    
            rr = min(res, rr)
        k += 1
    print(rr if rr > 0 else -1)
