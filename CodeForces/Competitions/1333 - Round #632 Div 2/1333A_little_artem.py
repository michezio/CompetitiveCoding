t = int(input())

answer = []

while (t):
    t -= 1

    row, col = [int(x) for x in input().split(" ")]
    b = 0
    w = 0

    grid = []
    for r in range(row):
        grid.append([])
        for c in range(col):
            if ((r + c) % 2 == 0):
                grid[r].append("B")
                b += 1
            else:
                grid[r].append("W")
                w += 1
    if (b == w):
        grid[0][1] = "B"

    answer.append(grid)

for a in answer:
    for r in a:
        print("".join(r))
