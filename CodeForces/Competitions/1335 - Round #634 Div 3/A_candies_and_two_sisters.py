# A

cases = int(input())

ans = []

while(cases):
    cases -= 1
    n = int(input())

    if n == 0:
        ans.append(0)
    elif n % 2 == 0:
        ans.append(n//2 - 1)
    else:
        ans.append(n//2)

for a in ans:
    print(a)
