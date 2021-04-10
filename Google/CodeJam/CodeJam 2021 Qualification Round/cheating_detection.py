import math

def solve(players):
    questions = [0] * 10_000
    for player in players:
        for i, ans in enumerate(player):
            questions[i] += ans
    # using the logit function (inverse of sigmoid)
    questions = list(map(lambda x: -math.log(0.01*x/(1-0.01*x)), questions))

    lowest_range = 10e9
    cheater = 0
    for index, player in enumerate(players):
        '''
        # calculate the ELO score of each player (not needed)
        elo = 0
        for i, q in enumerate(questions):
            ans = player[i]
            expected = 1.0 / (1 + math.exp(q - elo))
            elo = elo + 0.03 * (ans - expected)
        '''
        avg_wrong = 0
        avg_correct = 0
        wrong = 0
        for i, q in enumerate(questions):
            if player[i] == 0:
                wrong += 1
                avg_wrong += q
            else:
                avg_correct += q
        avg_wrong = avg_wrong / wrong
        avg_correct = avg_correct / (10_000 - wrong)
        rng = avg_wrong - avg_correct
        if wrong < 5_000 and rng < lowest_range:
            lowest_range = rng
            cheater = index
            
        if DEBUG:
            line = f"Player #{index+1}:\tAVG_WRONG: {int(avg_wrong*1000)}\tAVG_CORRECT: {int(avg_correct*1000)}\tRANGE: {int(rng*1000)}"
            print(line.expandtabs(13))
            
    return cheater


DEBUG = False

if DEBUG:

    with open("cheaters.in") as f:
        TEST = int(f.readline().strip())
        PERC = int(f.readline().strip())
        for case in range(TEST):
            players = []
            for _ in range(100):
                players.append([int(x) for x in f.readline().strip()])
            res = solve(players)
            print(f"Case #{case+1}: {res+1}")

else:

    TEST = int(input())
    PERC = int(input())
    for case in range(TEST):
        players = []
        for _ in range(100):
            players.append([int(x) for x in input()])
        res = solve(players)
        print(f"Case #{case+1}: {res+1}")
    