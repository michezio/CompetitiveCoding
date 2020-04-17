# B

cases = int(input())

letters = 'abcdefghijklmnopqrstuvwxyz'

ans = []

while(cases):
    cases -= 1

    n, a, b = [int(x) for x in input().split(" ")]

    st = letters[0:b]
    while(len(st) < a):
        st += st[-1]
    index = 0
    while(len(st) < n):
        st += st[index]
        index += 1

    ans.append(st)

for a in ans:
    print(a)
