TESTS = int(input())

for _ in range(TESTS):
    s = input()
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')

    if ((a+c) == b) or (a == b and c == 0) or (c == b and a == 0):
        print("YES")
    else:
        print("NO")
