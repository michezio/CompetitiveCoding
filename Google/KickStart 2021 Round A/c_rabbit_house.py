def floodBack(grid, i, j):
  if i == -1 or j == -1:
    return 0
  a = grid[i][j]
  added = 0
  if j>0 and grid[i][j-1] < a-1:
    diff = a-grid[i][j-1] -1
    grid[i][j-1] += diff
    added += diff + floodBack(grid, i, j-1)
  if i>0 and grid[i-1][j] < a-1:
    diff = a-grid[i-1][j] -1
    grid[i-1][j] += diff
    added += diff + floodBack(grid, i-1, j)
  return added
  
def flood(grid, i,j):
  added = 0
  a = grid[i][j]
  if j<len(grid[0])-1 and grid[i][j+1] < a-1:
    diff = a-grid[i][j+1] -1
    grid[i][j+1] += diff
    added += diff
  if i<len(grid)-1 and grid[i+1][j] < a-1:
    diff = a-grid[i+1][j] -1
    grid[i+1][j] += diff
    added += diff
  added += floodBack(grid, i, j)
  return added
  
def compute(grid):
  total = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      total += flood(grid, i, j)
  return total

results = []

cases_num = int(input())

for i in range(cases_num):
  R, C = [int(s) for s in input().split(" ")]
  grid = []
  for _ in range(R):
    grid.append([int(c) for c in input().split()])
  results.append(compute(grid))

case = 1
for num in results:
  print("Case #{}: {}".format(case, num))
  case += 1
