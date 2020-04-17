w = int(input())

ans = []

while(w):
    w -= 1
    J = None
    C = None
    minutes = []
    for j in range(24*60+1):
        minutes.append([])
    n = int(input())
    tasks = [""] * n
    for i in range(n):
        line = [int(x) for x in input().split(" ")]
        minutes[line[0]].append(i)
        minutes[line[1]].append(i)

    impossible = False
    for m in [x for x in minutes[:-1] if len(x) != 0]:
        if J in m:
            m.remove(J)
            J = None
        if C in m:
            m.remove(C)
            C = None
        for t in m:
            if J is None:
                J = t
                tasks[t] = "J"
            elif C is None:
                C = t
                tasks[t] = "C"
            else:
                impossible = True
                break
        if impossible:
            tasks = None
            break

    if tasks is None:
        ans.append("IMPOSSIBLE")
    else:
        st = "".join(tasks)
        ans.append(st)


for i in range(len(ans)):
    a = ans[i]
    print("Case #{}: {}".format(i+1, a))
