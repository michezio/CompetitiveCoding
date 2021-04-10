def group_split(line):
    groups = []
    temp = None
    for c in line:
        if (temp is None):
            temp = c
        elif (c == temp[-1]):
            temp += c
        else:
            groups.append(temp)
            temp = c
    groups.append(temp)
    return groups


w = int(input())

ans = []

while(w):
    w -= 1
    s = input()

    ''' TEST CASE 1
    groups = group_split(s)
    ss = ""
    for g in groups:
        if (g[0] == '1'):
            g = '({})'.format(g)
        ss += g
    ans.append(ss)
    '''

    s = [int(x) for x in s]
    s.append(0)
    res = ""
    prev = 0
    for n in s:
        diff = n - prev
        if (diff > 0):
            res += ('(' * diff)
        elif (diff < 0):
            res += (')' * -diff)
        res += str(n)
        prev = n

    ans.append(res[:-1])


for i in range(len(ans)):
    a = ans[i]
    print("Case #{}: {}".format(i+1, a))
