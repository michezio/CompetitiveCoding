'''
WORKS ONLY FOR FIRST TEST CASE
the path it finds aren't actually the shortest ones
'''

TEST = int(input())

for i in range(TEST):
    answer = ""
    x, y = [int(x) for x in input().split()]
    px = x > 0
    py = y > 0
    x = abs(x)
    y = abs(y)

    while (x > 0 or y > 0):
        if (x % 2 == y % 2):
            answer = "IMPOSSIBLE"
            break
        if (x >> 1) % 2 != (y >> 1) % 2 or (x == 0 or y == 0):
            if x % 2 == 1:
                answer += 'E' if px else 'W'
            else:
                answer += 'N' if py else 'S'
        else:
            if x % 2 == 1:
                answer += 'W' if px else 'E'
                x += 1
            else:
                answer += 'S' if py else 'N'
                y += 1
        x = x >> 1
        y = y >> 1

    print("Case #{}: {}".format(i+1, answer))
