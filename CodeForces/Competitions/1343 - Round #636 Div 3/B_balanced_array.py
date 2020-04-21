TEST = int(input())

answers = []
for _ in range(TEST):
    n = int(input())

    arr = []
    if (n >> 1) % 2 == 1:
        answers.append(["NO"])
    else:
        b = 1
        for i in range(n // 4):
            arr.append(b)
            arr.append(b+1)
            arr.append(b+3)
            arr.append(b+4)
            b += 6
        answers.append(["YES"])
        arr.sort(key=lambda x: x % 2 == 1)
        answers.append(arr)


for ans in answers:
    print(*ans)
