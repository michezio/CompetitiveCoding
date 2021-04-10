def getLs(a, b):
  resa = max(1,min(b, a//2))
  resb = max(1,min(a, b//2))
  return resa+resb-2

def compute(g):
  R = len(g)
  C = len(g[0])
  to_right = [[0] * C for _ in range(R)]
  to_left = [[0] * C for _ in range(R)]
  to_down = [[0] * C for _ in range(R)]
  to_up = [[0] * C for _ in range(R)]
  
  for i in range(R):
    for j in range(C):
      to_right[i][j] = to_right[i][j-1] + g[i][j] if g[i][j] == 1 else 0
      to_left[i][-j-1] = to_left[i][-j] + g[i][-j-1] if g[i][-j-1] == 1 else 0
      to_down[i][j] = to_down[i-1][j] + g[i][j] if g[i][j] == 1 else 0
      to_up[-i-1][j] = to_up[-i][j] + g[-i-1][j] if g[-i-1][j] == 1 else 0
  score = 0
  for i in range(R):
    for j in range(C):   
      u = to_down[i][j]
      d = to_up[i][j]
      l = to_right[i][j]
      r = to_left[i][j]
      if u>3 and (l>1 or r>1) or \
         d>3 and (l>1 or r>1) or \
         l>3 and (u>1 or d>1) or \
         r>3 and (u>1 or d>1):
        score += getLs(u, l) + getLs(u, r) + getLs(d, l) + getLs(d, r)
  return score


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
