import copy

TESTS = int(input())



def run(grid, check, k):
    
    vertex = []

    n = len(grid)
    m = len(grid[0])

    def inRange(x, y):
        return 0 <= x < m and 0 <= y < n

    def isConnected(grid, x, y):
        con = False
        if (inRange(x-1, y-1)):
            con |= grid[y-1][x-1]
        if (inRange(x-1, y+1)):
            con |= grid[y+1][x-1]
        if (inRange(x+1, y-1)):
            con |= grid[y-1][x+1]
        if (inRange(x+1, y+1)):
            con |= grid[y+1][x+1]
        return con

    def isVertex(grid, x, y, k):
        vert = True
        while (k > 0):
            if (inRange(x-k, y-k)):
                vert &= grid[y-k][x-k]
            else:
                return False
            if (inRange(x+k, y-k)):
                vert &= grid[y-k][x+k]
            else:
                return False
            k -= 1
        return vert

    def fill(grid, check, x, y):
        step = 1
        check[y][x] = True
        condition = True
        while (condition):
            condition = False
            if (inRange(x-step, y-step) and inRange(x+step, y-step)):
                if (grid[y-step][x-step] and grid[y-step][x+step]):
                    check[y-step][x-step] = True
                    check[y-step][x+step] = True
                    step += 1
                    condition = True
        
    
    for y in range(n):
        for x in range(m):
            if not grid[y][x]:
                continue
            if not isConnected(grid, x, y):
                return False
            if isVertex(grid, x, y, k):
                vertex.append((x, y))

    for x, y in vertex:
        fill(grid, check, x, y)

    for row in check:
        for el in row:
            if not el:
                return False
    return True



for _ in range(TESTS):

    n, m, k = map(int, input().split())
    
    grid = []
    check = []
    
    for i in range(n):
        grid.append([True if x == '*' else False for x in input()])
        check.append([not x for x in grid[-1]])
    
    res = run(grid, check, k)
    print("YES" if res else "NO")
