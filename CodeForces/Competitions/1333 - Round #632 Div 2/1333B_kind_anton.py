case = int(input())

answers = []

while (case):
    case -= 1

    L = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]

    possible = None

    if (L < 2):
        if (a[0] == b[0]):
            possible = "YES"
        else:
            possible = "NO"
    elif (a[0] != b[0]):
        possible = "NO"
    else:
        possible = "YES"
        one_before = a[0] == 1
        minus_before = a[0] == -1
        for i in range(1, L):
            aa = a[i]
            bb = b[i]
            q1 = aa < bb and one_before
            q2 = aa > bb and minus_before
            one_before |= a[i] == 1
            minus_before |= a[i] == -1
            if (aa == bb or q1 or q2):
                continue
            else:
                possible = "NO"
                break

    if (possible is not None):
        answers.append(possible)
    else:
        print("ERROR")
        exit()


for ans in answers:
    print(ans)
