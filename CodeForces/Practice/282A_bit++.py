# https://codeforces.com/problemset/problem/282/A
# 282A Bit++

w = int(input())

x = 0
while(w):
    w -= 1
    op = input()
    if (op[1] == "+"):
        x += 1
    elif (op[1] == "-"):
        x -= 1

print(x)
