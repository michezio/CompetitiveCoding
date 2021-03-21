''' Algorithm is working but gives wrong answer on test set 1
	so maybe it's not the optimal solution '''

def recoverRowCS(g, i):
  ind = g[i].index(False)
  g[i][ind] = True
  return ind

def tryRecoverRowCS(g, i):
  if g[i].count(False) == 1:
    ind = recoverRowCS(g, i)
    tryRecoverColCS(g, ind)

def recoverColCS(g, j, col):
  ind = col.index(False)
  g[ind][j] = True
  return ind

def tryRecoverColCS(g, j):
  col = [grid[p][j] for p in range(len(g))]
  if col.count(False) == 1:
    ind = recoverColCS(g, j, col)
    tryRecoverRowCS(g, ind)

def compute(g, w):
  total = 0
  m = len(g)
  for i in range(m):
    tryRecoverRowCS(g, i)
    tryRecoverColCS(g, i)
  while not all(all(x) for x in g):
    minW = 10e10
    x, y = 0, 0
    for i in range(m):
      for j in range(m):
        if g[i][j] == False and w[i][j] < minW:
          minW = w[i][j]
          x, y = i, j
    total += minW
    g[x][y] = True
    tryRecoverRowCS(g, x)
    tryRecoverColCS(g, y)
  return total
    
  
    
  
results = []

cases_num = int(input())

for i in range(cases_num):
  siz = int(input())
  grid = []
  for _ in range(siz):
    grid.append([False if x == '-1' else True for x in input().split()])
  weights = []
  for _ in range(siz):
    weights.append([int(x) for x in input().split()])
  input()
  input()
  results.append(compute(grid, weights))

case = 1
for num in results:
  print("Case #{}: {}".format(case, num))
  case += 1
