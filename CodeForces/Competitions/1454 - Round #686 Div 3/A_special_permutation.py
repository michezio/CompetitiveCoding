TEST = int(input())

answers = []
for _ in range(TEST):
    size = int(input())
    
    res = [x+1 for x in range(size)]
    res.append(res.pop(0))

    answers.append(res)

for ans in answers:
    print(*ans)