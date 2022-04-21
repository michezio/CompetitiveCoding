TESTS = int(input())

for _ in range(TESTS):

    l = int(input())

    letts = [x for x in input().split("W") if x != ""]

    if any((len(x) < 2 for x in letts)):
        print("NO")
        continue

    if all(("R" in chunk and "B" in chunk for chunk in letts)):
        print("YES")
    else:
        print("NO")
            