TEST = int(input())

answers = []
for _ in range(TEST):
    n = int(input())
    a = 3
    k = 2
    while (n % a != 0):
        a += 2**k
        k += 1

    answers.append(n // a)

for ans in answers:
    print(ans)
