TEST = int(input())

answers = []
for _ in range(TEST):
    n = int(input())
    moves = 0
    for i in range(1, n//2+1):
        moves += i * (i*2)

    answers.append(moves*4)

for ans in answers:
    print(ans)
