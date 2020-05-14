'''
THE ALGORITHM IS CORRECT
BUT ACTUALLY GIVING THE WRONG ANSWER FOR TEST CASE 2
don't know why and haven't been able to submit it
'''

TEST = int(input())

answers = []
for _ in range(TEST):
    rows, cols = [int(x) for x in input().split()]
    grid = []
    for i in range(rows):
        grid.append([int(x) for x in input().split()])

    costs = [[None for x in range(cols)] for y in range(rows)]
    rc = rows + cols - 2

    diff = abs(grid[-1][-1] - grid[0][0] - rc)
    if grid[-1][-1] > grid[0][0] + rc:
        costs[-1][-1] = diff
        grid[-1][-1] -= diff
    else:
        costs[0][0] = diff
        grid[0][0] -= diff

    start = grid[0][0]
    prev = lambda x, y: start + x + y
    for y in range(rows):
        for x in range(cols):
            if costs[y][x]:
                continue
            if grid[y][x] < prev(x, y):
                c = float("inf")
            else:
                c = grid[y][x] - prev(x, y)
            costs[y][x] = c

    dist = [[float("inf") for x in range(cols)] for y in range(rows)]
    for y in range(rows):
        for x in range(cols):
            act = costs[y][x]
            if y > 0 and x > 0:
                dist[y][x] = min(dist[y][x-1], dist[y-1][x]) + act
            elif x > 0:
                dist[y][x] = dist[y][x-1] + act
            elif y > 0:
                dist[y][x] = dist[y-1][x] + act
            else:
                dist[0][0] = act
    answers.append(dist[-1][-1])

for ans in answers:
    print(ans)
