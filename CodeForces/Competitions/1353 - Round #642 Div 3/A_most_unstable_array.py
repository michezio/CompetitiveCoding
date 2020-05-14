TEST = int(input())

answers = []
for _ in range(TEST):
    size, total = [int(x) for x in input().split()]
    if size == 1:
        answers.append(0)
        continue
    ans = total * (2 if size > 2 else 1)

    answers.append(ans)

for ans in answers:
    print(ans)
