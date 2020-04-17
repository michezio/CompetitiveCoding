CASES = int(input())

answers = []

while (CASES):
    possible = "YES"
    CASES -= 1
    pr_played = 0
    pr_cleared = 0
    N = int(input())
    for i in range(N):
        played, cleared = [int(x) for x in input().split(" ")]
        if (played < cleared or played < pr_played or cleared < pr_cleared
                # or (cleared > pr_cleared and played == pr_played)):
                or (cleared - pr_cleared > played - pr_played)):
            possible = "NO"
        pr_cleared = cleared
        pr_played = played

    answers.append(possible)

for ans in answers:
    print(ans)
